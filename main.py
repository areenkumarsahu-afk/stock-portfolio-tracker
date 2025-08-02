import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Portfolio Tracker",layout="wide")
st.title("Stock Portfolio Tracker")
uploaded_file=st.file_uploader("Upload your portfolio CSV",type="csv")

if uploaded_file:
    df=pd.read_csv(uploaded_file)

    results=[]
    total_value=0

    for i,row in df.iterrows():
        ticker=row.Ticker
        shares=row.Shares 
        buy_price=row.Buy_Price 

        stock=yf.Ticker(ticker)
        hist=stock.history(period="1d")

        if hist.empty:
            st.warning(f"No data found for {ticker}")
            continue
        current_price=hist.Close.iloc[-1]
        value=current_price*shares
        gain=(current_price-buy_price)*shares

        results.append({
            "Ticker":ticker,
            "Shares":shares,
            "Buy_Price":buy_price,
            "Current_Price":round(current_price,2),
            "Value":round(value,2),
            "Gain/Loss":round(gain,2)
        })
        total_value+=value
    result_df=pd.DataFrame(results)
    st.subheader("Portfolio Sumarry")
    st.write(result_df)
    st.subheader("Total Portfolio Value")
    st.metric("Total Value",f"${total_value:.2f}")
    st.subheader("Portfolio Breakdown")
    fig=go.Figure()
    fig.add_trace(go.Pie(labels=result_df.Ticker,values=result_df.Value,hole=.4))
    st.plotly_chart(fig,use_container_width=True)

else:
    st.info("Upload a CSV file with columns:Ticker,Shares,Buy_Price")