import yfinance as yf
import pandas as pd

dat = yf.Ticker("NU")
name = dat.info["displayName"]
hist = dat.history(period="1d")
price = round(hist["Close"].iloc[-1],2)

print(f"El precio actual de {name} es: {price}")
