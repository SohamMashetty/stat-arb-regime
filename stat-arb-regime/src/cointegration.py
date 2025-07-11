import statsmodels.api as sm
from statsmodels.tsa.stattools import coint
import pandas as pd

def cointegration_test(x, y, significance=0.05):
    score, pvalue, _ = coint(x, y)
    return pvalue < significance, pvalue

def compute_spread(x, y):
    x = sm.add_constant(x)
    model = sm.OLS(y, x).fit()
    beta = model.params[1]
    spread = y - beta * x.iloc[:,1]  # remove constant
    return spread, beta