import pandas as pd

def compute_zscore(spread, window=30):
    mean = spread.rolling(window=window).mean()
    std = spread.rolling(window=window).std()
    return (spread - mean) / std

def generate_signals(zscore, entry_threshold=1.0, exit_threshold=0.2):
    position = pd.Series(index=zscore.index, dtype=float)
    position[zscore > entry_threshold] = -1  # Short
    position[zscore < -entry_threshold] = 1  # Long
    position[abs(zscore) < exit_threshold] = 0  # Exit
    return position.ffill().fillna(0)