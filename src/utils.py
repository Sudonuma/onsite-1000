from sklearn.ensemble import RandomForestClassifier
import joblib
from typing import List, Union


import pandas as pd
import numpy as np


def load_data(dataset_path: str) -> pd.DataFrame:
    """
    Load data from a CSV file.

    Parameters:
    - dataset_path (str): The file path to the CSV dataset.

    Returns:
    - df (pd.DataFrame): The loaded DataFrame containing the dataset.
    """
    df = pd.read_csv(dataset_path)
    return df

def load_image_data():
    pass

def load_text_data():
    pass



def print_column_types(df: pd.DataFrame) -> None:
    """
    Print the names of numerical columns and categorical columns in a DataFrame.

    Parameters:
    - df (pd.DataFrame): The input DataFrame.
    """
    # Get column data types
    column_types = df.dtypes
    
    # Separate columns into numerical and categorical
    numerical_columns = column_types[column_types != 'object'].index.tolist()
    categorical_columns = column_types[column_types == 'object'].index.tolist()
    
    # Print the names of numerical columns
    print("Numerical columns:")
    for col in numerical_columns:
        print("-", col)
    
    # Print the names of categorical columns
    print("\nCategorical columns:")
    for col in categorical_columns:
        print("-", col)



def remove_nan_rows(df: pd.DataFrame) -> pd.DataFrame:
    """
    Check for NaN values in a DataFrame, print the number of NaN values,
    and remove rows containing NaN values.

    Parameters:
    - df (pd.DataFrame): The input DataFrame.

    Returns:
    - clean_df (pd.DataFrame): The DataFrame with NaN rows removed.
    """
    # Check for NaN values
    nan_count = df.isna().sum().sum()
    if nan_count > 0:
        print(f"Number of NaN values found: {nan_count}")
        
        # Remove rows with NaN values
        clean_df = df.dropna(axis=0)
        print("Rows with NaN values removed.")
        return clean_df
    else:
        print("No NaN values found in the DataFrame.")
        return df

def drop(df: pd.DataFrame, drop_columns: List[str])-> pd.DataFrame:
    """
    Drop specified columns from the DataFrame.

    Parameters:
    - df (pd.DataFrame): The input DataFrame.
    - drop_columns (List[str]): A list of column names to be dropped from the DataFrame.

    Returns:
    - df (pd.DataFrame): The DataFrame with specified columns dropped.
    """
    df = df.drop(columns=drop_columns)
    return df


def pre_process_data(df: pd.DataFrame) -> pd.DataFrame:
    pass


def train(train_data, target, model_path):
    pass

def inference(model_filename, test_set):

    with open(model_filename, 'rb') as f:
        loaded_model = joblib.load(f)

    return


