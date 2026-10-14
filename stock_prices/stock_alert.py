import yfinance as yf


TICKER = "NU"
TRADING_DAYS_YEAR = 252     # Dias de bolsa en un año aprox.
AVG_VOLUME_WINDOW = 63      # Dias de bolsa en 3 meses aprox.


def get_history(ticker, period="2y"):
    """Descarga el historico OHLCV. 2y para que la MA200 tenga datos suficientes."""
    hist = yf.Ticker(ticker).history(period=period)
    if hist.empty:
        raise ValueError(f"Sin datos para {ticker}: ticker invalido o Yahoo no respondio")
    return hist


def get_name(ticker):
    """Unico uso de .info: datos que NO estan en el historico. .get evita el KeyError."""
    try:
        return yf.Ticker(ticker).info.get("longName", ticker)
    except Exception:
        return ticker

def get_rsi(close):
    delta = close.diff()
    gains = delta.clip(lower=0)
    avg_gains = gains.rolling(window=14).mean()
    losses = - 1 * delta.clip(upper=0)
    avg_losses = losses.rolling(window=14).mean()
    rs = avg_gains / avg_losses
    rsi = 100 - (100 / (1+rs) )
    return rsi


# ---------------------------------------------------------------------------
# SEÑALES
# Supuestos: el analisis fundamental ya aprobo la accion (NU), asi que buscamos
# TIMING: comprar retrocesos dentro de una tendencia alcista y no atrapar
# "cuchillos cayendo". Horizonte: swing / posicional (semanas a pocos meses).
# OJO: tu RSI es el de media simple (Cutler), no el de Wilder; los umbrales son
# aproximados y deben validarse con backtest antes de confiar en ellos.
# ---------------------------------------------------------------------------
RSI_OVERSOLD = 35           # Zona de retroceso/sobreventa (30 es mas estricto y da menos señales)
RSI_OVERBOUGHT = 70         # Sobrecompra
NEAR_LOW_PCT = 0.35         # Precio en el 35% inferior del rango 52w = "barato" relativo
NEAR_HIGH_PCT = 0.85        # Precio en el 15% superior del rango 52w = cerca de maximos
VOLUME_RATIO_MIN = 1.2      # Volumen >= 1.2x el promedio = hay interes/capitulacion
EXTENDED_VS_MA50 = 1.15     # Precio 15% sobre la MA50 = estirado


def evaluate_signals(lp, ma50, ma200, rsi, last_volume, avg_volume, low_52w, high_52w):
    """Funcion pura: recibe numeros, devuelve la decision. Sin red ni prints (testeable).

    Prioridad de reglas:
      1. Datos insuficientes -> NO_DATA
      2. Tendencia rota (precio < MA200 y MA50 < MA200) -> SELL
      3. Tendencia alcista (precio > MA200) + retroceso confirmado -> BUY
      4. Sobrecompra cerca de maximos -> TAKE_PROFIT
      5. Resto -> HOLD (o WATCH si esta cerca de un setup de compra)
    """
    values = (lp, ma50, ma200, rsi, last_volume, avg_volume, low_52w, high_52w)
    if any(v != v for v in values):          # v != v solo es True para NaN
        return {"action": "NO_DATA", "score": 0, "reasons": ["Datos insuficientes (NaN)"]}

    range_52w = high_52w - low_52w
    pos_52w = (lp - low_52w) / range_52w if range_52w > 0 else 0.5   # 0 = minimo, 1 = maximo
    volume_ratio = last_volume / avg_volume if avg_volume > 0 else 0

    uptrend = lp > ma200
    trend_broken = lp < ma200 and ma50 < ma200

    # --- 2. SELL: la tesis tecnica se invalida ---
    if trend_broken:
        return {"action": "SELL", "score": 0,
                "reasons": [f"Tendencia rota: precio {lp:.2f} < MA200 {ma200:.2f} y MA50 {ma50:.2f} < MA200"]}

    # --- 3. BUY: filtro de tendencia + confirmaciones ---
    buy_checks = {
        f"RSI {rsi:.0f} <= {RSI_OVERSOLD} (retroceso/sobreventa)": rsi <= RSI_OVERSOLD,
        f"Precio {lp:.2f} <= MA50 {ma50:.2f} (pullback a la media)": lp <= ma50,
        f"Precio en el {pos_52w:.0%} inferior del rango 52w (barato relativo)": pos_52w <= NEAR_LOW_PCT,
        f"Volumen {volume_ratio:.1f}x el promedio (interes)": volume_ratio >= VOLUME_RATIO_MIN,
    }
    buy_score = sum(buy_checks.values())
    buy_reasons = [txt for txt, ok in buy_checks.items() if ok]

    if uptrend and rsi <= RSI_OVERSOLD and buy_score >= 2:
        return {"action": "BUY", "score": buy_score, "reasons": [f"Tendencia alcista: precio > MA200 {ma200:.2f}"] + buy_reasons}

    # --- 4. TAKE_PROFIT: sobrecompra + cerca de maximos / estirado ---
    sell_checks = {
        f"RSI {rsi:.0f} >= {RSI_OVERBOUGHT} (sobrecompra)": rsi >= RSI_OVERBOUGHT,
        f"Precio en el {pos_52w:.0%} del rango 52w (cerca de maximos)": pos_52w >= NEAR_HIGH_PCT,
        f"Precio {lp / ma50 - 1:.0%} sobre la MA50 (estirado)": lp >= ma50 * EXTENDED_VS_MA50,
    }
    sell_score = sum(sell_checks.values())
    if sell_score >= 2:
        return {"action": "TAKE_PROFIT", "score": sell_score, "reasons": [txt for txt, ok in sell_checks.items() if ok]}

    # --- 5. WATCH / HOLD ---
    if uptrend and (buy_score >= 1 or rsi <= 45):
        return {"action": "WATCH", "score": buy_score, "reasons": ["Tendencia alcista, retroceso aun incompleto"] + buy_reasons}
    if not uptrend:
        return {"action": "HOLD", "score": 0, "reasons": [f"Precio {lp:.2f} bajo MA200 {ma200:.2f}, pero sin ruptura confirmada: no comprar"]}
    return {"action": "HOLD", "score": 0, "reasons": ["Sin setup claro de compra ni de venta"]}


ACTION_LABELS = {
    "BUY": "COMPRA - setup de retroceso en tendencia alcista",
    "SELL": "VENTA - tendencia tecnica rota (reducir/salir si tienes posicion)",
    "TAKE_PROFIT": "TOMAR GANANCIAS - sobrecompra (considerar reducir posicion)",
    "WATCH": "VIGILAR - cerca de un setup de compra, aun no",
    "HOLD": "NO HACER NADA por ahora",
    "NO_DATA": "SIN DATOS suficientes para decidir",
}


def format_message(name, ticker, lp, rsi, ma50, ma200, result):
    """Arma el mensaje para el usuario final (aqui solo texto; el canal de envio es aparte)."""
    lines = [
        f"{name} ({ticker}) | Precio {lp:.2f} | RSI {rsi:.0f} | MA50 {ma50:.2f} | MA200 {ma200:.2f}",
        f"DECISION: {ACTION_LABELS[result['action']]}",
    ]
    lines += [f"  - {r}" for r in result["reasons"]]
    lines.append("Nota: señal tecnica automatica, no es asesoria financiera.")
    return "\n".join(lines)


def run_analisis(ticker=TICKER):
    hist = get_history(ticker)
    name = get_name(ticker)

    # Datos base, todos calculados desde hist (una sola fuente, definiciones bajo tu control)
    lp = hist["Close"].iloc[-1]                                          # Ultimo precio
    low_52w = hist["Low"].tail(TRADING_DAYS_YEAR).min()                  # Minimo 52 semanas (intradia)
    high_52w = hist["High"].tail(TRADING_DAYS_YEAR).max()                # Maximo 52 semanas (intradia)
    last_volume = hist["Volume"].iloc[-1]                                # Volumen del ultimo dia
    avg_volume = hist["Volume"].tail(AVG_VOLUME_WINDOW).mean()           # Volumen promedio 3 meses

    # Indicadores 
    moving_average_50 = hist["Close"].rolling(50).mean().iloc[-1]       
    moving_average_200 = hist["Close"].rolling(200).mean().iloc[-1]     
    rsi_series = get_rsi(hist["Close"])                                            
    rsi = rsi_series.iloc[-1]                             
    

    # Logica de señales
    result = evaluate_signals(lp, moving_average_50, moving_average_200, rsi,
                              last_volume, avg_volume, low_52w, high_52w)

    # Impresion de resultados
    print(format_message(name, ticker, lp, rsi, moving_average_50, moving_average_200, result))
    print(f"\nRango 52w: {low_52w:.2f} - {high_52w:.2f}")
    print(f"Volumen ultimo dia: {last_volume:,.0f} | promedio 3m: {avg_volume:,.0f}")


if __name__ == '__main__':
    run_analisis()
