import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import plotly.express as px

#run streamlit run nwhacks2023_0.py
st.title('Stock Dashboard')
ticker = st.sidebar.text_input('Ticker')
start_Date = st.sidebar.date_input('Start Date')
end_Date = st.sidebar.date_input('End Date')

data = yf.download(ticker, start=start_Date, end=end_Date)

pricing_data, norm = st.tabs(["Pricing Data", "norm"])

with pricing_data:
    fig = px.line(data, x = data.index, y = data['Adj Close'], title = ticker)
    st.plotly_chart(fig)

    st.header('Price Movements')
    data2 = data
    data2['% Change'] = data['Adj Close'] / data['Adj Close'].shift(1) - 1
    data2.dropna(inplace=True)
    st.write(data2)
    annual_return = data2['% Change'].mean() * 252 *100
    st.write('Annual Return is ', annual_return, '%')
    stdev = np.std(data2['% Change']) * np.sqrt(252)
    st.write('Standard Deviation is ', stdev*100, '%')
    st.write('Risk adj. Return is ', annual_return/(stdev*100))

with norm:
    fig2 = px.line(data, x = data.index, y = data['Close'], title = ticker)
    st.plotly_chart(fig2)