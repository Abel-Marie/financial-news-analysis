import matplotlib.pyplot as plt

def plot_stock_data_with_indicators(df, stock_name):
    """
    Plots stock price and technical indicators.
    Args:
        df (pd.DataFrame): DataFrame containing stock price data and indicators.
        stock_name (str): Name of the stock.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(df['Close'], label='Close Price', color='blue')
    plt.plot(df['SMA_50'], label='50-Day SMA', color='orange')
    plt.plot(df['SMA_200'], label='200-Day SMA', color='green')
    plt.title(f"{stock_name} Close Price with SMA")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.legend()
    plt.grid()
    plt.show()

def plot_rsi(df, stock_name):
    """
    Plots the RSI (Relative Strength Index).
    """
    plt.figure(figsize=(12, 4))
    plt.plot(df['RSI'], label='RSI', color='purple')
    plt.axhline(70, linestyle='--', color='red', label='Overbought')
    plt.axhline(30, linestyle='--', color='green', label='Oversold')
    plt.title(f"{stock_name} Relative Strength Index (RSI)")
    plt.legend()
    plt.show()

def plot_macd(df, stock_name):
    """
    Plots MACD and Signal Line.
    """
    plt.figure(figsize=(12, 4))
    plt.plot(df['MACD'], label='MACD', color='blue')
    plt.plot(df['MACD_signal'], label='Signal Line', color='orange')
    plt.title(f"{stock_name} MACD and Signal Line")
    plt.legend()
    plt.show()
