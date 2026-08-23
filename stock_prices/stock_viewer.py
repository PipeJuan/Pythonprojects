import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


dat = yf.Ticker("^GSPC")
name = dat.info["longName"]
hist = dat.history(period="max")
#price = round(hist["Close"].iloc[-1],2)
#price_last_month = hist.resample('YE').last()
price_per_month = hist["Close"].resample('ME').last()

plt.plot(price_per_month)
plt.show()



#print(dat.info)
#print(price_per_year.tail())

