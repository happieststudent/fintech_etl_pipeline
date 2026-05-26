# src/transform.py
import yfinance as yf
import pandas as pd

def fetch_and_clean_data(tickers, start_date, end_date):
    print(f"Downloading data for {tickers}...")
    
    # Download data and extract ONLY the 'Close' prices for all tickers
    raw_data = yf.download(tickers, start=start_date, end=end_date)['Close']
    
    # Cleaning Step: 
    # ffill() forward-fills Friday's stock price into Sat/Sun blanks
    # dropna() removes any remaining empty rows at the very beginning of the dataset
    clean_data = raw_data.ffill().dropna()
    
    print(f"Data cleaned. Total missing values remaining: {clean_data.isnull().sum().sum()}")
    return clean_data

if __name__ == "__main__":
    # A mix of Tech, Market Index, EV, Crypto, and Bonds
    portfolio = ["AAPL", "SPY", "TSLA", "BTC-USD", "TLT"]
    
    # Fetch data for the year 2023
    df = fetch_and_clean_data(portfolio, "2023-01-01", "2024-01-01")
    
    # Display the first 5 rows to verify it worked
    print("\nCleaned Portfolio Data:")
    print(df.head())