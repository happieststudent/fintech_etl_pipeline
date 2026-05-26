# main.py
from src.transform import fetch_and_clean_data
from src.metrics import calculate_daily_returns, calculate_sharpe_ratio
from src.load import save_to_database
import matplotlib.pyplot as plt

def run_pipeline():
    portfolio = ["AAPL", "SPY", "TSLA", "BTC-USD", "TLT"]
    
    try:
        print("--- STARTING ETL PIPELINE ---")
        
        # 1. EXTRACT & TRANSFORM
        prices = fetch_and_clean_data(portfolio, "2023-01-01", "2024-01-01")
        
        # 2. ANALYZE
        returns = calculate_daily_returns(prices)
        sharpe = calculate_sharpe_ratio(returns)
        print("\nCalculated Sharpe Ratios:\n", sharpe)
        
        # 3. LOAD
        save_to_database(prices, returns)
        
        # 4. VISUALIZE
        print("\nGenerating portfolio chart...")
        prices.plot(figsize=(10, 5), title="Portfolio Asset Prices (2023)")
        plt.savefig('portfolio_chart.png')
        print("Chart saved as portfolio_chart.png!")
        
        print("--- PIPELINE COMPLETE ---")
        
    except Exception as e:
        print(f"Pipeline failed: {e}")

if __name__ == "__main__":
    run_pipeline()