from src.data_loader import load_data
from src.preprocess import preprocess_data


df = load_data()

print("Before preprocessing:")
print(df.dtypes)

df = preprocess_data(df)

print("\nAfter preprocessing:")
print(df.dtypes)

print("\nFirst 5 dates:")
print(df["date"].head())

print("\nProcessed columns:")
print(df.columns.tolist())

print("\nProcessed data:")
print(df[["date", "time", "month", "day", "day_of_week", "hour"]].head())

print("\nMissing values after preprocessing:")
print(df.isnull().sum())

print("\nDuplicate rows after preprocessing:")
print(df.duplicated().sum())

print("\nHour range:")
print(df["hour"].min(), "to", df["hour"].max())

print("\nMonth values:")
print(df["month"].unique())

print("\nDay of week values:")
print(df["day_of_week"].unique())