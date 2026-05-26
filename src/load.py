# src/load.py
import sqlite3
import pandas as pd

def save_to_database(prices_df, returns_df, db_name="portfolio.db"):
    # Create a connection to SQLite (this creates the file if it doesn't exist)
    conn = sqlite3.connect(db_name)
    
    print(f"Saving data to {db_name}...")
    
    # df.to_sql automatically creates the SQL table and inserts the data!
    prices_df.to_sql('historical_prices', conn, if_exists='replace')
    returns_df.to_sql('daily_returns', conn, if_exists='replace')
    
    conn.close()
    print("Data successfully saved to SQL!")

if __name__ == "__main__":
    # Import our previous work to test the load pipeline
    from transform import fetch_and_clean_data
    from metrics import calculate_daily_returns
    
    portfolio = ["AAPL", "SPY", "TSLA", "BTC-USD", "TLT"]
    
    # 1. Extract & Transform
    prices = fetch_and_clean_data(portfolio, "2023-01-01", "2024-01-01")
    
    # 2. Analyze
    returns = calculate_daily_returns(prices)
    
    # 3. Load
    save_to_database(prices, returns)