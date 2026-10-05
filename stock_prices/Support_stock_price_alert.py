"""Archivo de exploracion de la API de yfinance (no es parte del flujo final)."""
import yfinance as yf


def explore(ticker="NU"):
    stocks = yf.Ticker(ticker)

    # Ver que claves existen en los diccionarios de la libreria
    # print(list(stocks.fast_info.keys()))
    # print(list(stocks.info.keys()))
    # help(stocks.info)

    print(stocks.news)


if __name__ == '__main__':
    explore()
