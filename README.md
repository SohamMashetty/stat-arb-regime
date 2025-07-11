Statistical Arbitrage with Regime Detection
This project implements a statistical arbitrage strategy using cointegration and Hidden Markov Models (HMMs) to identify market regimes and build trading signals. Inspired by systematic trading practices used in firms like Optiver, the pipeline is built entirely from scratch with interpretability and modularity in mind.

Highlights

Fetch historical stock data via yfinance

Detect cointegrated pairs using OLS regression & Augmented Dickey-Fuller tests

Model spread behavior using Gaussian Hidden Markov Models

Generate regime-based trading signals

Evaluate performance with Sharpe ratio, drawdown, and cumulative PnL
