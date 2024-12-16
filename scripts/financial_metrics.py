from pynance import metrics

def calculate_financial_metrics(df):
    """
    Calculates cumulative return, Sharpe ratio, and volatility.
    Args:
        df (pd.DataFrame): DataFrame containing 'Close' column.
    Returns:
        dict: A dictionary of calculated metrics.
    """
    df['Daily Return'] = df['Close'].pct_change()
    cumulative_return = metrics.cumret(df['Daily Return'])
    sharpe_ratio = metrics.sharpe(df['Daily Return'], rf=0.02)
    volatility = df['Daily Return'].std()

    return {
        'Cumulative Return': cumulative_return[-1],
        'Sharpe Ratio': sharpe_ratio,
        'Volatility': volatility
    }
