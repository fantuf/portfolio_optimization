import pandas as pd
import yfinance as yf
import plotly.express as px
import streamlit as st

# Fetch data from the saved CSV file
data = pd.read_csv("portfolio_data.csv", index_col="Date", parse_dates=True)

# text input for weights and symbols
symbols = st.text_input("Enter stock tickers (comma-separated):", "AAPL, MSFT, TSLA")
symbols_list = [s.strip() for s in symbols.split(",")]
weights = st.text_input("Enter portfolio weights (comma-separated):", "0.4, 0.3, 0.3")
weights_list = [float(w) for w in weights.split(",")]

# Normalize prices and calculate daily portfolio value
normalized_data = data / data.iloc[0]
portfolio_values = (normalized_data * weights_list).sum(axis=1)

# Calculate cumulative returns
cumulative_returns = portfolio_values / portfolio_values.iloc[0] - 1

# Line chart for portfolio performance
st.subheader("Portfolio Performance")
st.line_chart(portfolio_values)

# Pie chart for asset allocation
allocation_df = pd.DataFrame({
    "Symbol": symbols_list,
    "Weight": weights_list
})
fig = px.pie(allocation_df, values="Weight", names="Symbol", title="Portfolio Allocation")
st.plotly_chart(fig)

# Daily returns and volatility
daily_returns = portfolio_values.pct_change().dropna()
volatility = daily_returns.std() * (252 ** 0.5)  # Annualized volatility
sharpe_ratio = daily_returns.mean() / daily_returns.std() * (252 ** 0.5)

# Display metrics
st.subheader("Risk Metrics")
st.write(f"Annualized Volatility: {volatility:.2%}")
st.write(f"Sharpe Ratio: {sharpe_ratio:.2f}")
