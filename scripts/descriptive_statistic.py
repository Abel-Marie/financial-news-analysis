import pandas as pd
import numpy as np



def dataset_summary(df):
    """
    Provides a summary of the dataset, including rows, columns, missing values, and data types.
    """
    summary = {
        "Total Rows": df.shape[0],
        "Total Columns": df.shape[1],
        "Missing Values": df.isnull().sum().to_dict(),
        "Data Types": df.dtypes.to_dict()
    }
    return summary

def compute_basic_stats(df):
    """
    Computes median, mode, and trimmed mean for headline lengths.
    """
    lengths = df['headline'].str.len()
    median = np.median(lengths)
    mode = lengths.mode()[0]
    trimmed_mean = lengths.clip(lower=lengths.quantile(0.05), upper=lengths.quantile(0.95)).mean()
    return {'median': median, 'mode': mode, 'trimmed_mean': trimmed_mean}


def count_unique_symbols(df):
    """
    Counts unique stock ticker symbols and their frequencies.
    """
    return df['stock'].value_counts()




