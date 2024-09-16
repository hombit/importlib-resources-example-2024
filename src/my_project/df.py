from importlib.resources import open_binary

import pandas as pd

import my_project.data


def my_df():
    """Get the data"""
    with open_binary(my_project.data, "table.csv") as f:
        return pd.read_csv(f)
