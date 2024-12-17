import pandas as pd

def preprocess_stock_data(df):
    """
    Cleans and preprocesses the stock data.
    Args:
        df (pd.DataFrame): Raw stock DataFrame.
    Returns:
        pd.DataFrame: Preprocessed stock DataFrame.
    """
    # Convert Date to datetime
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Drop duplicates
    df = df.drop_duplicates()
    
    # Handle missing values with forward and backward fill
    df = df.groupby('Stock').apply(lambda group: group.ffill().bfill()).reset_index(drop=True)
    
    # Drop rows with critical missing values
    df = df.dropna(subset=['Close', 'Volume'])
    
    # Add daily return as a new feature
    df['Daily_Return'] = df.groupby('Stock')['Close'].pct_change()
    
    return df
