# Portfolio Optimization Dashboard

An interactive **Streamlit** dashboard to analyze portfolio performance, allocation, and basic risk metrics using historical price data.

This project provides a simple framework to compute portfolio returns, annualized volatility, and Sharpe ratio, and to visualize performance dynamically.

---

## Overview

The application:

- Loads historical price data from a CSV file
- Allows the user to input:
  - Asset tickers
  - Portfolio weights
- Computes:
  - Portfolio cumulative return
  - Annualized volatility
  - Sharpe ratio (risk-free rate assumed 0)
- Displays:
  - Portfolio performance time series
  - Allocation pie chart

This project is designed as a lightweight foundation for portfolio analytics and can be extended toward more advanced quantitative optimization techniques.

---

## Tech Stack

- Python
- Streamlit
- Pandas
- Plotly

---

## Installation

Clone the repository:

```bash
git clone https://github.com/fantuf/portfolio_optimization.git
cd portfolio_optimization
