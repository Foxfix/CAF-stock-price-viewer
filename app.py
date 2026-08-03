import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime

st.title('Stock Price Viewer')
st.sidebar.header('Enter your symbols of stocks')
stock_symbol1 = st.sidebar.text_input('Enter the symbol of the first stock (for example, AAPL for Apple)')
stock_symbol2 = st.sidebar.text_input('Enter the symbol of another promotion (for example, MSFT for Microsoft)')

start_year, end_year = st.sidebar.slider(
    'Select the ramge of years: ',
    min_value=2000, max_value=datetime.now().year, value=(2015, 2020)
)
if stock_symbol1 and stock_symbol2:
    start_date = f"{start_year}-01-01"
    end_date = f"{end_year}-12-31"

    stock_data1 = yf.download(stock_symbol1, start=start_date, end=end_date)
    stock_data2 = yf.download(stock_symbol2, start=start_date, end=end_date)

    if not stock_data1.empty and not stock_data2.empty:
        st.write('Financial data for the first share', stock_data1.head())
        st.write('Financial data for another promotion', stock_data2.head())

        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(stock_data1.index, stock_data1['Close'], label=f'Share price {stock_symbol1}')
        ax.plot(stock_data2.index, stock_data2['Close'], label=f'Share price {stock_symbol2}')
        ax.set_title('Share price chart')
        ax.set_xlabel('Date')
        ax.set_ylabel('Share price (USD)')
        ax.grid(True)
        ax.legend()

        st.pyplot(fig)
    else:
        st.error('No data found for the promotion symbols entered. ')


        