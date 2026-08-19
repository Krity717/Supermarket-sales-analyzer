def calculate_revenue_metrics(df):
    """Calculate overall revenue metrics."""

    total_revenue = df["revenue"].sum()
    average_revenue = df["revenue"].mean()

    return {
        "total_revenue": total_revenue,
        "average_revenue": average_revenue
    }

def revenue_by_branch(df):
    """Calculate total revenue for each branch."""

    return df.groupby("branch")["revenue"].sum().sort_values(ascending=False)

def revenue_by_product_line(df):
    """Calculate total revenue for each product line."""

    return df.groupby("product_line")["revenue"].sum().sort_values(ascending=False)

def revenue_by_customer_type(df):
    """Calculate total revenue by customer type."""

    return df.groupby("customer_type")["revenue"].sum().sort_values(ascending=False)


def revenue_by_gender(df):
    """Calculate total revenue by gender."""

    return df.groupby("gender_customer")["revenue"].sum().sort_values(ascending=False)

def revenue_by_payment_method(df):
    """Calculate total revenue by payment method."""

    return df.groupby("payment_method")["revenue"].sum().sort_values(ascending=False)

def revenue_by_month(df):
    """Calculate total revenue for each month."""

    return df.groupby("month")["revenue"].sum().sort_index()

def revenue_by_day_of_week(df):
    """Calculate total revenue for each day of the week."""

    day_order = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]

    result = df.groupby("day_of_week")["revenue"].sum()

    return result.reindex(day_order)

def revenue_by_hour(df):
    """Calculate total revenue for each hour of the day."""

    return df.groupby("hour")["revenue"].sum().sort_index()

def average_rating_by_branch(df):
    """Calculate average customer rating for each branch."""

    return df.groupby("branch")["rating"].mean().sort_values(ascending=False)

def average_rating_by_product_line(df):
    """Calculate average customer rating for each product line."""

    return df.groupby("product_line")["rating"].mean().sort_values(ascending=False)