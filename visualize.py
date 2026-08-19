from src.data_loader import load_data
from src.preprocess import preprocess_data
from src.analysis import revenue_by_branch, revenue_by_product_line, revenue_by_customer_type, revenue_by_gender, revenue_by_payment_method
from src.visualization import plot_revenue_by_branch, plot_revenue_by_product_line, plot_revenue_by_customer_type, plot_revenue_by_gender, plot_revenue_by_payment_method


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