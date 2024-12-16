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


def load_yfinance_data(directory_path):
    """
    Load multiple CSV files from a directory into a single DataFrame.
    Args:
        directory_path (str): The path to the directory containing the CSV files.
    Returns:
        pd.DataFrame: A combined DataFrame with a 'Stock' column indicating the stock ticker.
    """
    all_data = []  
    file_names = os.listdir(directory_path)

    for file_name in file_names:
        if file_name.endswith('.csv'):  
            try:
                
                stock_name = file_name.split('_')[0].upper()
                file_path = os.path.join(directory_path, file_name)
                
                # Load the file
                df = pd.read_csv(file_path)
                df['Stock'] = stock_name  
                all_data.append(df)  
            except Exception as e:
                print(f"Error loading file {file_name}: {e}")

    
    if all_data:
        combined_df = pd.concat(all_data, ignore_index=True)
        return combined_df
    else:
        raise ValueError("No CSV files found or failed to load.")
