import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
from urllib.parse import urlparse

def top_publishers(df, top_n=10):
    """
    Identifies the top publishers contributing the most to the news feed.
    Args:
        df (pd.DataFrame): DataFrame containing 'publisher' column.
        top_n (int): Number of top publishers to return.
    Returns:
        pd.Series: A Series of top publishers and their article counts.
    """
    publisher_counts = df['publisher'].value_counts()
    top_publishers = publisher_counts.head(top_n)

    # Plotting
    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_publishers.values, y=top_publishers.index, palette='viridis')
    plt.title(f"Top {top_n} Publishers by Article Count")
    plt.xlabel("Number of Articles")
    plt.ylabel("Publishers")
    plt.show()

    return top_publishers

def email_domain_analysis(df):
    """
    Analyzes email-based publishers to extract unique domains and their contribution frequency.
    Args:
        df (pd.DataFrame): DataFrame containing 'publisher' column.
    Returns:
        pd.Series: A Series of email domains and their article counts.
    """
    # Extract email-based publishers
    email_publishers = df['publisher'][df['publisher'].str.contains('@', na=False)]
    
    # Extract domains from email addresses
    domains = email_publishers.str.split('@').str[-1]

    # Count frequency of domains
    domain_counts = domains.value_counts()

    # Plotting
    plt.figure(figsize=(10, 6))
    sns.barplot(x=domain_counts.head(10).values, y=domain_counts.head(10).index, palette='coolwarm')
    plt.title("Top 10 Email Domains by Article Count")
    plt.xlabel("Number of Articles")
    plt.ylabel("Email Domains")
    plt.show()

    return domain_counts

def news_type_analysis(df, keyword_list=None):
    """
    Analyzes the type of news reported by different publishers.
    Args:
        df (pd.DataFrame): DataFrame containing 'publisher' and 'headline' columns.
        keyword_list (list): List of keywords to analyze (e.g., ['FDA', 'approval', 'target']).
    Returns:
        pd.DataFrame: A DataFrame summarizing keyword occurrence by publisher.
    """
    if not keyword_list:
        keyword_list = ['FDA', 'approval', 'price target', 'earnings', 'dividend', 'stock upgrade']

    # Create a keyword count column for each publisher
    keyword_counts = {}
    for keyword in keyword_list:
        keyword_counts[keyword] = df['headline'].str.contains(keyword, case=False, na=False).groupby(df['publisher']).sum()

    keyword_df = pd.DataFrame(keyword_counts)

    # Normalize counts by the total articles for each publisher
    total_articles = df['publisher'].value_counts()
    keyword_df = keyword_df.divide(total_articles, axis=0).fillna(0)

    # Plot the top contributors for each keyword
    for keyword in keyword_list:
        keyword_df[keyword].sort_values(ascending=False).head(10).plot(kind='barh', figsize=(10, 6), title=f"Top Publishers Reporting on '{keyword}'")
        plt.xlabel("Normalized Frequency")
        plt.ylabel("Publishers")
        plt.show()

    return keyword_df

def unique_publishers_over_time(df):
    """
    Analyzes the trend of unique publishers contributing over time.
    Args:
        df (pd.DataFrame): DataFrame containing 'publisher' and 'date' columns.
    """
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df = df.dropna(subset=['date'])  # Remove invalid dates

    # Group by day and count unique publishers
    unique_publishers = df.groupby(df['date'].dt.date)['publisher'].nunique()

    # Plotting
    plt.figure(figsize=(12, 6))
    plt.plot(unique_publishers, marker='o', linestyle='-', color='teal')
    plt.title("Unique Publishers Over Time")
    plt.xlabel("Date")
    plt.ylabel("Number of Unique Publishers")
    plt.grid()
    plt.show()

    return unique_publishers

def publisher_domain_analysis(df):
    """
    Identifies unique domains contributing news based on publisher names that are URLs.
    Args:
        df (pd.DataFrame): DataFrame containing 'publisher' column.
    Returns:
        pd.Series: A Series of unique domains and their article counts.
    """
    # Extract domains from publishers that look like URLs
    url_publishers = df['publisher'][df['publisher'].str.contains('http', na=False)]
    domains = url_publishers.apply(lambda x: urlparse(x).netloc)

    domain_counts = domains.value_counts()

    # Plotting
    plt.figure(figsize=(10, 6))
    sns.barplot(x=domain_counts.head(10).values, y=domain_counts.head(10).index, palette='magma')
    plt.title("Top 10 Domains Contributing News")
    plt.xlabel("Number of Articles")
    plt.ylabel("Domains")
    plt.show()

    return domain_counts
