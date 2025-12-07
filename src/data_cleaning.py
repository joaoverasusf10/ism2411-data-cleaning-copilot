"""
Sales Data Cleaning Script
This script cleans messy sales data and saves it to a new file.
"""

import pandas as pd


def load_data(file_path):
    """
    Load the CSV file into a pandas DataFrame.
    We need to read the raw data before we can clean it.
    """
    # Copilot helped generate this function
    df = pd.read_csv(file_path)
    return df


def clean_column_names(df):
    """
    Make column names lowercase and replace spaces with underscores.
    This makes the columns easier to work with in Python.
    """
    # Copilot suggested this approach
    df.columns = df.columns.str.lower()
    df.columns = df.columns.str.replace(' ', '_')
    return df


def handle_missing_values(df):
    """
    Remove rows that have missing prices or quantities.
    We can't analyze sales without knowing the price and quantity.
    """
    df = df.dropna(subset=['price', 'quantity'])
    return df


def remove_invalid_rows(df):
    """
    Remove rows with negative prices or negative quantities.
    Negative numbers don't make sense for sales data - they are errors.
    """
    df = df[df['price'] >= 0]
    df = df[df['quantity'] >= 0]
    return df


if __name__ == "__main__":
    raw_path = "data/raw/sales_data_raw.csv"
    cleaned_path = "data/processed/sales_data_clean.csv"

    df_raw = load_data(raw_path)
    df_clean = clean_column_names(df_raw)
    df_clean = handle_missing_values(df_clean)
    df_clean = remove_invalid_rows(df_clean)
    df_clean.to_csv(cleaned_path, index=False)
    
    print("Cleaning complete. First few rows:")
    print(df_clean.head())