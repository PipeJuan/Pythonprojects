# Stock Prices

Proyecto para practicar Python aplicado a mercados de acciones. Puede contener errores.

## Objetivo
Alerta personalizada de precio: evaluar con reglas explicitas si es buen momento para comprar una accion.

## Archivos
- `stock_alert.py`: script principal (datos -> indicadores -> señales -> resultado).
- `stock_viewer.py`: grafico de cierre mensual de un ticker.
- `Support_stock_price_alert.py`: exploracion de la API de yfinance (no es flujo final).

## Decisiones de diseño
- Fuente unica: todo se calcula desde `history()`. `.info` solo para datos que no estan en el historico (nombre).
- `period="2y"` para que la MA200 tenga datos.

## Pendiente
- Indicadores: MA50, MA200, RSI(14).
- Definir reglas de compra y backtestearlas.
- Canal de alerta (Telegram/email) y programacion.

## Referencias
- Documentacion de yfinance: https://ranaroussi.github.io/yfinance/index.html
- Referencia avanzada: https://ranaroussi.github.io/yfinance/reference/index.html
