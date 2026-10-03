import yfinance as yf
import pandas as pd





def run_analisis():
    stocks = yf.Ticker("NU")
    name = stocks.info["longName"]
    hist = stocks.history(period="1d")
    news = stocks.news


    # Con esto puedo consultar que hay en los diccionarios de la libreria 
    #for key in stocks.fast_info.keys():
        #print(key)


    #print(help(stocks.info))
    print(news)
    




if __name__ == '__main__':
    run_analisis()




