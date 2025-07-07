import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# Download data
ticker = str(input("Please enter the ticker for the stock you'd like to analyse. FOr example, the ticker for Apple would be 'AAPL': ")) # Choose any stock
span = str(input("What date would you like to start the analysis from? Please use the format YYYY-MM-DD: "))
data = yf.download(ticker, start=span, end=datetime.today().strftime('%Y-%m-%d'))

if data.empty:
    print("Could not download data for the specified ticker and date range. Please check the ticker symbol and start date.")
else:
    data['Return'] = data['Close'].diff() # Calculating daily returns
    data['Momentum'] = data['Return'].rolling(20).mean() # Calculate 20-day rolling momentum
    data['Signal'] = np.where(data['Momentum'] > 0, 1, 0) # Positive signal if Momentum > 0, else 0
    data['Strategy_Return'] = data['Signal'].shift(1) * data['Return'] # Calculate strategy returns
    data = data.dropna()

    if data.empty:
        print("DataFrame is empty after dropping NaN values. Cannot proceed with calculations and plotting.")
    else:
        data['Cumulative_Strategy'] = data['Strategy_Return'].cumsum()
        data['Cumulative_BuyHold'] = data['Return'].cumsum()

        plt.figure(figsize=(12,6))
        plt.plot(data.index, data['Cumulative_Strategy'], label='Momentum Strategy')
        plt.plot(data.index, data['Cumulative_BuyHold'], label='Buy & Hold')
        plt.legend()
        plt.title('Strategic returns are {}, compared to Buy & Hold returns of {}'.format(round(data['Cumulative_Strategy'].iloc[-1],2),round(data['Cumulative_BuyHold'].iloc[-1],2)))
        plt.show()