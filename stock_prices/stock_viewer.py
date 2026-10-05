import yfinance as yf
import matplotlib.pyplot as plt


def plot_monthly_close(ticker="^GSPC"):
    hist = yf.Ticker(ticker).history(period="max")
    if hist.empty:
        raise ValueError(f"Sin datos para {ticker}")
    price_per_month = hist["Close"].resample('ME').last()

    plt.plot(price_per_month)
    plt.title(f"{ticker} - cierre mensual")
    plt.show()


if __name__ == '__main__':
    plot_monthly_close()
