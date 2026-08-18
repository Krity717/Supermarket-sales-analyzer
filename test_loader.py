from src.data_loader import load_data


df = load_data()

print("First 5 rows:")
print(df.head())

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("\nStatistical summary:")
print(df.describe())

print("\nUnique values:")

print("\nBranches:")
print(df["branch"].unique())

print("\nCities:")
print(df["city"].unique())

print("\nCustomer types:")
print(df["customer_type"].unique())

print("\nGender:")
print(df["gender_customer"].unique())

print("\nProduct lines:")
print(df["product_line"].unique())

print("\nPayment methods:")
print(df["payment_method"].unique())

print("\nDate range:")
print(df["date"].min(), "to", df["date"].max())