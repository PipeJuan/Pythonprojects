import yfinance as yf
import pandas as pd





def run_analisis():
    stocks = yf.Ticker("NU")
    name = stocks.info["longName"]
    hist = stocks.history(period="1y")
    lp = hist["Close"].iloc[-1]                                 # Ultimo precio
    range52w = stocks.info["fiftyTwoWeekRange"]         # 52 week low price de ese ultimo dia                                  
    regularvolume = stocks.info["regularMarketVolume"]  # Volumen regular de transaciones
    volume = stocks.info["averageVolume"]               #volumen de transacción del ultimo dia 
    
    # Indicadores 
    moving_averga_50 = 0                                # Media movil de 50 dias atras 
    moving_averga_200 = 0                               # Media movil de 200 dias atras 
    news = 0                                            # Traer las ultimas news relacioandas a la acción
    rsi = 0                                             # Saca el RSI de la acción del ultimo dia 


    # Logica de señales 


    # Impresión de resultados
    print(lp)
    print(range52w)
    print(regularvolume,volume)
    




if __name__ == '__main__':
    run_analisis()




