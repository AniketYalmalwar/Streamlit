import yfinance as yf
import streamlit as st
import pandas as pd

st.write("# Stock Price App")

tickerSymbol = "GOOGL"

tickerData = yf.Ticker(tickerSymbol)

tickerOf = tickerData.history(period='1d',start='2010-5-31',end="2020-5-31")

st.line_chart(tickerOf.Close)
st.line_chart(tickerOf.Volume)

