import pandas as pd
import os

def load_csv(file_path: str) -> pd.DataFrame:
    """
    Load a CSV file into a DataFrame.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded DataFrame.
    """
    try:
        df = pd.read_csv(file_path)
        print(f"Loaded data from {file_path}. Shape: {df.shape}")
        return df
    except Exception as e:
        print(f"Error loading file {file_path}: {e}")
        return pd.DataFrame()

def load_yfinance_data(folder_path: str) -> dict:
    """
    Load multiple CSV files from a folder containing YFinance data.

    Args:
        folder_path (str): Path to the folder.

    Returns:
        dict: A dictionary where keys are stock names and values are DataFrames.
    """
    data_dict = {}
    try:
        for file in os.listdir(folder_path):
            if file.endswith('.csv'):
                stock_name = os.path.splitext(file)[0]
                file_path = os.path.join(folder_path, file)
                data_dict[stock_name] = pd.read_csv(file_path)
                print(f"Loaded {stock_name} data. Shape: {data_dict[stock_name].shape}")
    except Exception as e:
        print(f"Error loading data from folder {folder_path}: {e}")
    return data_dict
