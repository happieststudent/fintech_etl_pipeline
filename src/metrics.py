# src/metrics.py
import pandas as pd
import numpy as np

def calculate_daily_returns(clean_data):
    # pct_change() automatically calculates (Today - Yesterday) / Yesterday
    # dropna() removes the first row because it has no "Yesterday" to compare to
    returns = clean_data.pct_change().dropna()
    return returns

def calculate_sharpe_ratio(daily_returns, risk_free_rate=0.0):
    # Annualized Sharpe Ratio = (Mean Return / Std Dev) * sqrt(252 trading days)
    mean_return = daily_returns.mean()
    std_dev = daily_returns.std()
    
    sharpe_ratio = ((mean_return - risk_free_rate) / std_dev) * np.sqrt(252)
    return sharpe_ratio

if __name__ == "__main__":
    # Import the function we wrote in Phase 2!
    from transform import fetch_and_clean_data
    
    portfolio = ["AAPL", "SPY", "TSLA", "BTC-USD", "TLT"]
    df = fetch_and_clean_data(portfolio, "2023-01-01", "2024-01-01")
    
    # Calculate our metrics
    returns = calculate_daily_returns(df)
    sharpe = calculate_sharpe_ratio(returns)
    
    print("\n--- Sharpe Ratios ---")
    print(sharpe.sort_values(ascending=False))

    python src/metrics.py
    