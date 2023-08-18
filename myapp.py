import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App
Welcome to the Simple Stock Price App! This app displays the historical **closing price** and ***volume*** of Google's stock (ticker symbol: GOOGL).

If you're curious about how Google's stock has performed over time, you're in the right place. You can explore the closing price and volume trends using interactive charts below.
""")
# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
# Define the ticker symbol
tickerSymbol = 'GOOGL'
# Get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
# Get the historical prices for this ticker
historicalPrices = tickerData.history(period='max')

st.write("""
## Closing Price
In the following chart, you can observe the historical trend of Google's closing prices. This data represents the price at which Google's stock closed each trading day.
""")
st.line_chart(historicalPrices.Close)
st.write("""
## Volume
The following chart displays the historical volume of Google's stock, which indicates the number of shares that were traded each day. Volume can provide insights into the level of market interest and activity in the stock.
""")
st.line_chart(historicalPrices.Volume)

st.write("""
## Summary
In summary, this app allows you to visualize and explore the historical closing prices and trading volumes of Google's stock. By observing trends in closing prices, you can gain insights into the overall performance of the stock over time. Similarly, analyzing trading volumes can offer clues about market sentiment and interest in the stock.

Feel free to interact with the charts to zoom in on specific time periods or to closely examine changes in stock prices and volumes. Please note that past performance may not necessarily predict future trends in the stock market.
""")

