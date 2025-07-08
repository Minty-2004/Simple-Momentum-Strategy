# Simple Momentum Strategy Backtest

## Overview

This project implements and backtests a **simple momentum trading strategy** using Python. The strategy is based on the principle that stocks with positive recent returns (momentum) are likely to continue performing well in the near future.

---

## Strategy Logic

1. **Calculate daily returns** for the chosen stock.
2. **Calculate a rolling average return** over a window of N days (e.g. 20-day momentum).
3. **Generate trading signals**:
   - **Long position (buy)** if the rolling average return is positive.
   - **Hold cash (no position)** otherwise.
4. **Backtest the strategy performance** and compare it to a buy-and-hold benchmark.

---

## Technologies Used

- **Python 3**
- `pandas` for data manipulation
- `numpy` for numerical calculations
- `matplotlib` for data visualisation
- `yfinance` for downloading historical stock data
- `datetime` for selecting time frames

---

## Results

The backtest plots:

- **Cumulative returns** of the momentum strategy.
- **Cumulative returns** of the buy-and-hold strategy.

This allows visual and quantitative evaluation of the strategy's performance against a passive benchmark.

---

## How to Run

1. Clone this repository
2. Install dependencies (see requirements.txt)
3. Run the script (main.py)

---

## Example Output

<img width="1111" alt="Example Output" src="https://github.com/user-attachments/assets/70bc9f4b-d815-4084-a1e5-c94569079766" />

---

## Possible Extensions (potentially implemented by me in future projects)

- Optimise the rolling window (N) for maximum Sharpe ratio.
- Apply the strategy to multiple stocks and build a portfolio.
- Include **transaction costs** to assess real-world profitability.
- Use **log returns** for numerical stability in calculations.
- Calculate **annualised returns and standard deviation** for risk-adjusted analysis.

---

## Purpose

This project was created as the first step of my journey into Financial Analysis with Python. It demonstrates:

- Financial data analysis with Python
- Implementation of a classic momentum strategy
- Backtesting and performance comparison skills

---

## Author

**Muhammad Muntasir Shahzad**  
Student at King's College London, University of London. Studying Mathematics with Management and Finance   
Graduating: Summer 2026  
[LinkedIn Profile](www.linkedin.com/in/muntasir-shahzad) | [Email](muntasir.s.2004@gmail.com)

Please don't hesitate to contact me if you have any questions, suggestions, or otherwise.

---

## Disclaimer

This code is for educational purposes only and does not constitute financial advice or an investment recommendation.

