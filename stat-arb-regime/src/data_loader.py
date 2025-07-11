import pandas as pd
import yfinance as yf
import os

def fetch_and_save_sample_data(ticker_x='HDFCBANK.NS', ticker_y='ICICIBANK.NS',
                               start='2023-01-01', end='2024-01-01',
                               output_path='data/raw/sample.csv'):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    x = yf.download(ticker_x, start=start, end=end)["Close"]
    y = yf.download(ticker_y, start=start, end=end)["Close"]

    if x.empty or y.empty:
        raise ValueError("Downloaded data is empty. Check ticker symbols or date range.")

    df = pd.concat([x, y], axis=1)
    df.columns = ["StockX", "StockY"]
    df.dropna(inplace=True)

    if df.empty:
        raise ValueError("After dropping NaNs, no data remains. Try different tickers or wider date range.")

    df.index.name = 'Date'
    df.to_csv(output_path)
    print(f" Sample data saved to {output_path}")

def load_price_data(file_path='data/raw/sample.csv'):
    df = pd.read_csv(file_path, parse_dates=["Date"], index_col="Date")
    df = df.sort_index()
    return df

def preprocess(df):
    df = df.dropna()
    df = df[df.columns[:2]]  # Assume first two columns are asset prices
    return df