import pandas as pd


def preprocess_data(df):
    """Clean and prepare the supermarket sales data."""

    df = df.copy()

    # Convert date and time to datetime
    df["date"] = pd.to_datetime(df["date"], format="mixed")
    df["time"] = pd.to_datetime(df["time"], format="%H:%M")

    # Create useful date features
    df["month"] = df["date"].dt.month
    df["day"] = df["date"].dt.day
    df["day_of_week"] = df["date"].dt.day_name()

    # Create hour feature
    df["hour"] = df["time"].dt.hour

    return df