import pandas as pd
import numpy as np


def load_data(file_path):
    """Loads data from a CSV file."""
    return pd.read_csv(file_path)


def preprocess_data(data):
    """Preprocesses the input data for analysis."""
    # Example preprocessing steps
    data.dropna(inplace=True)  # Removing missing values
    data['date'] = pd.to_datetime(data['date'])  # Converting date column to datetime
    data = data[(data['value'] > 0)]  # Filtering out negative values
    return data
