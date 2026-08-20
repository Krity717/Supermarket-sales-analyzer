from src.data_loader import load_data
from src.preprocess import preprocess_data
from src.analysis import (
    calculate_revenue_metrics,
    revenue_by_branch,
    revenue_by_product_line,
    revenue_by_customer_type,
    revenue_by_gender,
    revenue_by_payment_method,
    revenue_by_month,
    revenue_by_day_of_week,
    revenue_by_hour,
    average_rating_by_branch,
    average_rating_by_product_line
)


df = load_data()
df = preprocess_data(df)

metrics = calculate_revenue_metrics(df)

print("Revenue Metrics:")
print(f"Total Revenue: {metrics['total_revenue']:.2f}")
print(f"Average Revenue: {metrics['average_revenue']:.2f}")

print("\nRevenue by Branch:")
print(revenue_by_branch(df))

print("\nRevenue by Product Line:")
print(revenue_by_product_line(df))

print("\nRevenue by Customer Type:")
print(revenue_by_customer_type(df))

print("\nRevenue by Gender:")
print(revenue_by_gender(df))

print("\nRevenue by Payment Method:")
print(revenue_by_payment_method(df))

print("\nRevenue by Month")
print(revenue_by_month(df))

print("\nRevenue by Day of Week:")
print(revenue_by_day_of_week(df))

print("\nRevenue by Hour:")
print(revenue_by_hour(df))

print("\nAverage Rating by Branch:")
print(average_rating_by_branch(df))

print("\nAverage Rating by Product Line:")
print(average_rating_by_product_line(df))

# Basic tests
assert len(df) > 0
assert metrics["total_revenue"] > 0
assert metrics["average_revenue"] > 0

assert len(revenue_by_branch(df)) > 0
assert len(revenue_by_product_line(df)) > 0
assert len(revenue_by_customer_type(df)) > 0
assert len(revenue_by_gender(df)) > 0
assert len(revenue_by_payment_method(df)) > 0
assert len(revenue_by_month(df)) > 0
assert len(revenue_by_day_of_week(df)) > 0
assert len(revenue_by_hour(df)) > 0
assert len(average_rating_by_branch(df)) > 0
assert len(average_rating_by_product_line(df)) > 0

print("\nAll tests passed!")