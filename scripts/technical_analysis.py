import talib

def add_technical_indicators(df):
    """
    Add technical indicators to the stock data using TA-Lib.
    Args:
        df (pd.DataFrame): Preprocessed stock DataFrame.
    Returns:
        pd.DataFrame: Stock DataFrame with technical indicators.
    """
    indicators = []  # To collect processed data
    for stock in df['Stock'].unique():
        print(f"Processing stock: {stock}")  # Debugging stock loop
        subset = df[df['Stock'] == stock].copy()

        # Check if 'Close' column exists
        if 'Close' not in subset.columns:
            raise ValueError(f"'Close' column missing for stock {stock}")

        # Moving Averages
        subset['SMA_10'] = talib.SMA(subset['Close'], timeperiod=10)
        subset['SMA_50'] = talib.SMA(subset['Close'], timeperiod=50)

        # Relative Strength Index (RSI)
        subset['RSI'] = talib.RSI(subset['Close'], timeperiod=14)

        # Moving Average Convergence Divergence (MACD)
        macd, macd_signal, _ = talib.MACD(subset['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
        subset['MACD'] = macd
        subset['MACD_Signal'] = macd_signal

        print(subset[['Date', 'Close', 'SMA_10', 'SMA_50', 'RSI', 'MACD']].tail())  # Check calculations

        indicators.append(subset)

    # Combine all processed data
    result = pd.concat(indicators)
    return result
