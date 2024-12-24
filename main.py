import streamlit as st
import yfinance as yf

st.write(
    '''
## Stock Price App :
'''
)

ticker_symbol=st.text_input("Enter the company ticker symbol (GOOGL,AAPL,MSFT)","GOOGL")

if ticker_symbol:
    ticker_data=yf.Ticker(ticker_symbol)

    try:
        tickerDf=ticker_data.history(period='1d',start="2010-05-31",end="2020-05-31")

        if not tickerDf.empty:
            st.write("Closing Price")
            st.line_chart(tickerDf.Close)

            st.write("Volume  Price")
            st.line_chart(tickerDf.Volume)
        else:
            st.write("No histortical data")

    except Exception as e:
        st.write("An error occurred")

else:
    st.write("Please enter a valid symbol")

