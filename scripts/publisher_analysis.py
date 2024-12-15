import pandas as  pd

def top_publishers(df):
    """
    Identifies publishers contributing the most to the news feed.
    """
    return df['publisher'].value_counts()

def publisher_sentiment_analysis(df):
    """
    Computes average sentiment scores for each publisher.
    """
    return df.groupby('publisher')['sentiment_score'].mean()
# def count_articles_per_publisher(df):
#     """
#     Counts the number of articles per publisher and creates a ranked list.
#     """
#     return df['publisher'].value_counts()