import pandas as pd

def backtest(spread, position):
    returns = pd.Series(spread).diff().fillna(0)
    pnl = returns * position
    cum_return = pnl.cumsum()
    sharpe = pnl.mean() / pnl.std() * (252**0.5)
    drawdown = cum_return.cummax() - cum_return
    max_dd = drawdown.max()
    return pd.DataFrame({'pnl': pnl, 'sharpe': sharpe, 'max_dd': max_dd}, index=returns.index)