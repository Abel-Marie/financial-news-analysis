from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
from sklearn.feature_extraction.text import TfidfVectorizer
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import networkx as nx
import spacy

def sentiment_analysis_vader(df):
    """
    Performs sentiment analysis using VADER.
    Adds a 'vader_sentiment' column to the DataFrame.
    """
    analyzer = SentimentIntensityAnalyzer()
    df['vader_sentiment'] = df['headline'].apply(lambda x: analyzer.polarity_scores(x)['compound'])
    return df

def sentiment_analysis_textblob(df):
    """
    Performs sentiment analysis using TextBlob.
    Adds a 'textblob_sentiment' column to the DataFrame.
    """
    df['textblob_sentiment'] = df['headline'].apply(lambda x: TextBlob(x).sentiment.polarity)
    return df

def combined_sentiment(df):
    """
    Combines VADER and TextBlob sentiment into a single average column.
    Categorizes sentiment into Positive, Neutral, and Negative.
    """
    df['combined_sentiment'] = df[['vader_sentiment', 'textblob_sentiment']].mean(axis=1)
    
    # Categorize sentiment
    df['sentiment_category'] = df['combined_sentiment'].apply(
        lambda x: 'Positive' if x > 0.2 else ('Negative' if x < -0.2 else 'Neutral')
    )
    return df

def sentiment_by_stock(df):
    """
    Aggregates sentiment scores by stock symbol.
    """
    sentiment_summary = df.groupby('stock')[['vader_sentiment', 'textblob_sentiment', 'combined_sentiment']].mean()
    return sentiment_summary

def generate_wordcloud(df, stock=None):
    """
    Generates a word cloud from headlines.
    If 'stock' is provided, filters headlines for the specific stock.
    """
    if stock:
        text = " ".join(df[df['stock'] == stock]['headline'])
        title = f"Word Cloud for Stock: {stock}"
    else:
        text = " ".join(df['headline'])
        title = "Word Cloud for All Headlines"

    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(title)
    plt.show()

def analyze_ngrams(df, n=2, top_n=10):
    """
    Analyzes n-grams (bi-grams or tri-grams) using TF-IDF.
    Plots the top N n-grams as a bar chart.
    """
    vectorizer = TfidfVectorizer(ngram_range=(n, n), stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(df['headline'])
    scores = zip(vectorizer.get_feature_names_out(), tfidf_matrix.sum(axis=0).tolist()[0])
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)[:top_n]

    # Plot results
    ngrams, values = zip(*sorted_scores)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=list(values), y=list(ngrams), palette="viridis")
    plt.title(f"Top {top_n} {n}-Grams")
    plt.xlabel("TF-IDF Score")
    plt.ylabel("N-Grams")
    plt.show()

    return sorted_scores

def extract_topics_from_headlines(df, top_n=10):
    """
    Extracts significant topics or events from headlines using TF-IDF.
    Filters for common phrases like 'FDA approval', 'price target', etc.
    """
    keywords = ['FDA approval', 'price target', '52-week high', 'earnings report', 'dividend', 'stock upgrade']
    filtered_df = df[df['headline'].str.contains('|'.join(keywords), case=False, na=False)]
    
    print(f"=== Extracted Topics (Top {top_n} Significant Headlines) ===")
    print(filtered_df[['headline', 'stock']].head(top_n))

    return filtered_df

def perform_ner(df):
    """
    Performs Named Entity Recognition (NER) and counts entity types.
    """
    nlp = spacy.load("en_core_web_sm")
    entity_counter = {}

    for doc in df['headline'].apply(nlp):
        for ent in doc.ents:
            entity_counter[ent.label_] = entity_counter.get(ent.label_, 0) + 1

    # Plot Entity Frequencies
    plt.figure(figsize=(10, 6))
    sns.barplot(x=list(entity_counter.keys()), y=list(entity_counter.values()), palette="muted")
    plt.title("Named Entity Recognition - Entity Frequencies")
    plt.xlabel("Entity Type")
    plt.ylabel("Count")
    plt.show()

    return entity_counter

def plot_sentiment_distribution(df):
    """
    Plots the distribution of sentiment scores.
    """
    plt.figure(figsize=(10, 6))
    sns.histplot(df['combined_sentiment'], bins=30, kde=True, color='blue')
    plt.title("Sentiment Score Distribution")
    plt.xlabel("Sentiment Score")
    plt.ylabel("Frequency")
    plt.show()

def filter_by_keywords(df, keywords):
    """
    Filters the DataFrame to include only rows with specified keywords in the headline.
    """
    filtered_df = df[df['headline'].str.contains('|'.join(keywords), case=False, na=False)]
    return filtered_df
