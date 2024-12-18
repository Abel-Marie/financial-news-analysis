# import pynance as pn

# def get_financial_metrics(df):
#     """
#     Fetch financial metrics such as cumulative returns and volatility.
#     Args:
#         df (pd.DataFrame): Preprocessed stock DataFrame.
#     Returns:
#         pd.DataFrame: DataFrame with financial metrics.
#     """
#     metrics = []
#     for stock in df['Stock'].unique():
#         subset = df[df['Stock'] == stock].copy()

#         # Calculate cumulative returns
#         subset['Cumulative_Return'] = (1 + subset['Daily_Return']).cumprod()

#         # Fetch volatility (standard deviation of returns)
#         subset['Volatility'] = subset['Daily_Return'].rolling(window=30).std()

#         metrics.append(subset)

#     return pd.concat(metrics)

import pandas as pd  
import pynance as pn

def get_financial_metrics(df):
    """
    Fetch financial metrics such as cumulative returns and volatility.
    Args:
        df (pd.DataFrame): Preprocessed stock DataFrame.
    Returns:
        pd.DataFrame: DataFrame with financial metrics.
    """
    metrics = []
    for stock in df['Stock'].unique():
        subset = df[df['Stock'] == stock].copy()

        # Calculate cumulative returns
        subset['Cumulative_Return'] = (1 + subset['Daily_Return']).cumprod()

        # Fetch volatility (standard deviation of returns)
        subset['Volatility'] = subset['Daily_Return'].rolling(window=30).std()

        metrics.append(subset)

    return pd.concat(metrics)  # Combine all stock data
