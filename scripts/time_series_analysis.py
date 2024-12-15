import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose
import numpy as np

def publication_frequency_analysis(df, freq='D', highlight_events=None):
    """
    Analyzes publication frequency over time and identifies spikes.
    Args:
        df (pd.DataFrame): DataFrame containing 'date' column.
        freq (str): Frequency for resampling ('D' for daily, 'W' for weekly, 'M' for monthly).
        highlight_events (dict): Optional dictionary of {date: event} for marking specific events.
    """
    df['publication_date'] = pd.to_datetime(df['date']).dt.date
    publication_counts = df['publication_date'].value_counts().sort_index()

    # Resample publication frequency
    resampled_counts = publication_counts.resample(freq).sum()

    plt.figure(figsize=(12, 6))
    plt.plot(resampled_counts, marker='o', linestyle='-', label=f'Publication Frequency ({freq})')

    # Highlight spikes/events
    if highlight_events:
        for date, event in highlight_events.items():
            plt.axvline(pd.to_datetime(date), color='red', linestyle='--', alpha=0.7)
            plt.text(pd.to_datetime(date), max(resampled_counts) * 0.8, event, rotation=90, color='red')

    plt.title(f"Publication Frequency Over Time ({freq} Resample)")
    plt.xlabel("Date")
    plt.ylabel("Number of Articles")
    plt.legend()
    plt.grid()
    plt.show()

def stl_decomposition(df, freq=30):
    """
    Performs STL decomposition on publication frequency.
    Args:
        df (pd.DataFrame): DataFrame containing 'date' column.
        freq (int): Seasonality period for STL decomposition.
    """
    df['publication_date'] = pd.to_datetime(df['date']).dt.date
    publication_counts = df['publication_date'].value_counts().sort_index()

    # Perform STL decomposition
    decomposition = seasonal_decompose(publication_counts, model='additive', period=freq)
    decomposition.plot()
    plt.suptitle("STL Decomposition of Publication Frequency", fontsize=14)
    plt.show()

def time_of_day_analysis(df):
    """
    Analyzes publication times and visualizes using heat maps.
    Args:
        df (pd.DataFrame): DataFrame containing 'date' column.
    """
    df['hour'] = pd.to_datetime(df['date']).dt.hour

    # Create a heatmap for hourly publication frequency
    hour_counts = df['hour'].value_counts().sort_index()

    plt.figure(figsize=(10, 6))
    sns.heatmap(hour_counts.values.reshape(-1, 1), annot=True, fmt='d', cmap="YlGnBu", cbar=False)
    plt.title("Hourly Publication Frequency")
    plt.xlabel("Hour of the Day")
    plt.ylabel("Publication Count")
    plt.yticks([])  # Remove y-ticks
    plt.show()

def moving_average_analysis(df, window=7):
    """
    Computes and visualizes moving averages to smooth publication frequency.
    Args:
        df (pd.DataFrame): DataFrame containing 'date' column.
        window (int): Window size for the moving average.
    """
    df['publication_date'] = pd.to_datetime(df['date']).dt.date
    publication_counts = df['publication_date'].value_counts().sort_index()

    # Calculate moving average
    moving_avg = publication_counts.rolling(window=window).mean()

    plt.figure(figsize=(12, 6))
    plt.plot(publication_counts, label="Daily Publication Count", alpha=0.6)
    plt.plot(moving_avg, label=f"{window}-Day Moving Average", color='orange')
    plt.title(f"Moving Average of Publication Frequency ({window}-Day Window)")
    plt.xlabel("Date")
    plt.ylabel("Number of Articles")
    plt.legend()
    plt.grid()
    plt.show()

def weekday_analysis(df):
    """
    Analyzes the frequency of publications by day of the week.
    Args:
        df (pd.DataFrame): DataFrame containing 'date' column.
    """
    df['weekday'] = pd.to_datetime(df['date']).dt.day_name()

    # Aggregate counts by day of the week
    weekday_counts = df['weekday'].value_counts()
    ordered_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    weekday_counts = weekday_counts.reindex(ordered_days)

    plt.figure(figsize=(10, 6))
    sns.barplot(x=weekday_counts.index, y=weekday_counts.values, palette="viridis")
    plt.title("Publication Frequency by Day of the Week")
    plt.xlabel("Day of the Week")
    plt.ylabel("Number of Articles")
    plt.show()
