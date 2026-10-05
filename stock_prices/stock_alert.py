import yfinance as yf
import pandas_ta as ta 

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


def run_analisis(ticker=TICKER):
    hist = get_history(ticker)
    name = get_name(ticker)

    # Datos base, todos calculados desde hist (una sola fuente, definiciones bajo tu control)
    lp = hist["Close"].iloc[-1]                                          # Ultimo precio
    low_52w = hist["Low"].tail(TRADING_DAYS_YEAR).min()                  # Minimo 52 semanas (intradia)
    high_52w = hist["High"].tail(TRADING_DAYS_YEAR).max()                # Maximo 52 semanas (intradia)
    last_volume = hist["Volume"].iloc[-1]                                # Volumen del ultimo dia
    avg_volume = hist["Volume"].tail(AVG_VOLUME_WINDOW).mean()           # Volumen promedio 3 meses

    # Indicadores (pendientes)
    moving_average_50 = hist["Close"].rolling(50).mean().iloc[-1]       
    moving_average_200 = hist["Close"].rolling(200).mean().iloc[-1]     
    rsi = ta.rsi(hist["Close"],14).iloc[-1]                             # TODO: RSI(14) del ultimo dia, calcularlo mejor manual 
    news = 0                                                            # TODO: ultimas noticias (stocks.news), mejor como contexto que como condicion

    # Logica de señales
    # TODO: definir reglas explicitas de compra

    # Impresion de resultados
    print(f"{name} ({ticker})")
    print(f"Ultimo precio: {lp:.2f}")
    print(f"Rango 52w: {low_52w:.2f} - {high_52w:.2f}")
    print(f"Volumen ultimo dia: {last_volume:,.0f} | promedio 3m: {avg_volume:,.0f}")


if __name__ == '__main__':
    run_analisis()
