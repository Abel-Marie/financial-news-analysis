import talib

def add_technical_indicators(df):
    """
    Add technical indicators to the stock data using TA-Lib.
    Args:
        df (pd.DataFrame): Preprocessed stock DataFrame.
    Returns:
        pd.DataFrame: Stock DataFrame with technical indicators.
    """
    indicators = []
    for stock in df['Stock'].unique():
        subset = df[df['Stock'] == stock].copy()

        # Moving Averages
        subset['SMA_10'] = talib.SMA(subset['Close'], timeperiod=10)
        subset['SMA_50'] = talib.SMA(subset['Close'], timeperiod=50)

        # Relative Strength Index (RSI)
        subset['RSI'] = talib.RSI(subset['Close'], timeperiod=14)

        # Moving Average Convergence Divergence (MACD)
        subset['MACD'], subset['MACD_Signal'], _ = talib.MACD(subset['Close'], fastperiod=12, slowperiod=26, signalperiod=9)

        indicators.append(subset)
    
    return pd.concat(indicators)
