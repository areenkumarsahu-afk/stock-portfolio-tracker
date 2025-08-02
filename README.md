# Stock Portfolio Tracker
This is a simple Streamlit web app that lets you upload your stock portfolio in CSV format and visualises the current market value using 'yfinance', 'pandas', and 'plotly'

## Features
- Upload a CSV file containing stock tickers and shar counts
- Fetch real-time prices using Yahoo Finance
- Calculate total value of portfolio
- Visualise it interactively with Plotly

## How to Run
'''bash
git clone https://github.com/areenkumarsahu-afk/stock-portfolio-tracker.git
cd stck-portfolio-tracker
pip install -r requirements.txt
streamlit run main.py