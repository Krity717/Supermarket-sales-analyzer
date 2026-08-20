from src.data_loader import load_data
from src.preprocess import preprocess_data
from src.analysis import revenue_by_branch, revenue_by_product_line, revenue_by_customer_type, revenue_by_gender, revenue_by_payment_method, revenue_by_month, revenue_by_day_of_week, revenue_by_hour, average_rating_by_branch, average_rating_by_product_line
from src.visualization import plot_revenue_by_branch, plot_revenue_by_product_line, plot_revenue_by_customer_type, plot_revenue_by_gender, plot_revenue_by_payment_method, plot_revenue_by_month, plot_revenue_by_day, plot_revenue_by_hour, plot_rating_by_branch, plot_rating_by_product


df = load_data()
df = preprocess_data(df)

branch_revenue = revenue_by_branch(df)

plot_revenue_by_branch(branch_revenue)

df = load_data()
df = preprocess_data(df)

branch_revenue = revenue_by_branch(df)
plot_revenue_by_branch(branch_revenue)

product_line_revenue = revenue_by_product_line(df)
plot_revenue_by_product_line(product_line_revenue)

customer_type_revenue = revenue_by_customer_type(df)

plot_revenue_by_customer_type(customer_type_revenue)

gender_revenue = revenue_by_gender(df)

plot_revenue_by_gender(gender_revenue)

payment_revenue = revenue_by_payment_method(df)

plot_revenue_by_payment_method(payment_revenue)

month_revenue = revenue_by_month(df)

plot_revenue_by_month(month_revenue)

day_revenue = revenue_by_day_of_week(df)

plot_revenue_by_day(day_revenue)

hour_revenue = revenue_by_hour(df)

plot_revenue_by_hour(hour_revenue)

branch_rating = average_rating_by_branch(df)

plot_rating_by_branch(branch_rating)

product_rating = average_rating_by_product_line(df)

plot_rating_by_product(product_rating)