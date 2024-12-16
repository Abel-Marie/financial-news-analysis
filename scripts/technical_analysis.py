import talib

def add_technical_indicators(df):
    """
    Adds technical indicators (SMA, RSI, MACD) to a stock DataFrame.
    Args:
        df (pd.DataFrame): DataFrame containing stock price data with 'Close' column.
    Returns:
        pd.DataFrame: DataFrame with added indicator columns.
    """
    df['SMA_50'] = talib.SMA(df['Close'], timeperiod=50)
    df['SMA_200'] = talib.SMA(df['Close'], timeperiod=200)
    df['RSI'] = talib.RSI(df['Close'], timeperiod=14)
    df['MACD'], df['MACD_signal'], _ = talib.MACD(df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
    return df
