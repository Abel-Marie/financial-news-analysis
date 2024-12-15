import matplotlib.pyplot as plt
import seaborn as sns
def plot_stock_data(stock_df):
    """Plot closing prices and technical indicators."""
    plt.figure(figsize=(14,7))
    plt.plot(stock_df['Close'], label='Close Price', color='blue')
    plt.plot(stock_df['SMA_20'], label='20 Day SMA', color='orange')
    plt.plot(stock_df['SMA_50'], label='50 Day SMA', color='red')
    plt.title('Stock Price and Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

def plot_rsi(stock_df):
    """Plot the Relative Strength Index (RSI)."""
    plt.figure(figsize=(14,7))
    plt.plot(stock_df['RSI'], label='RSI', color='purple')
    plt.title('Relative Strength Index (RSI)')
    plt.axhline(70, linestyle='--', alpha=0.5, color='red')  # Overbought
    plt.axhline(30, linestyle='--', alpha=0.5, color='green')  # Oversold
    plt.show()

def plot_macd(stock_df):
    """Plot MACD and Signal Line."""
    plt.figure(figsize=(14,7))
    plt.plot(stock_df['MACD'], label='MACD', color='blue')
    plt.plot(stock_df['MACD_signal'], label='Signal Line', color='orange')
    plt.title('MACD and Signal Line')
    plt.show()