import matplotlib.pyplot as plt


def plot_revenue_by_branch(branch_revenue):
    """Create a bar chart of revenue by branch."""

    plt.figure(figsize=(8, 5))

    branch_revenue.plot(kind="bar", color="gray")

    plt.title("Revenue by Branch")
    plt.xlabel("Branch")
    plt.ylabel("Revenue")

    plt.tight_layout()
    plt.savefig("images/revenue_by_branch.png")
    plt.show()

def plot_revenue_by_product_line(product_line_revenue):
    """Create a bar chart of revenue by product line."""

    plt.figure(figsize=(10, 6))

    product_line_revenue.plot(kind="barh", color="gray")

    plt.title("Revenue by Product Line")
    plt.xlabel("Revenue")
    plt.ylabel("Product Line")

    plt.tight_layout()
    plt.savefig("images/revenue_by_product_line.png")
    plt.show()

def plot_revenue_by_customer_type(customer_type_revenue):
    """Create a bar chart of revenue by customer type."""

    plt.figure(figsize=(8, 5))

    customer_type_revenue.plot(
        kind="bar",
        color=["skyblue", "gray"]
    )

    plt.title("Revenue by Customer Type")
    plt.xlabel("Customer Type")
    plt.ylabel("Revenue")

    plt.tight_layout()
    plt.savefig("images/revenue_by_customer_type.png")
    plt.show()

def plot_revenue_by_gender(gender_revenue):
    """Create a bar chart of revenue by gender."""

    plt.figure(figsize=(8, 5))

    gender_revenue.plot(
        kind="bar",
        color=["pink", "skyblue"]
    )

    plt.title("Revenue by Gender")
    plt.xlabel("Gender")
    plt.ylabel("Revenue")

    plt.tight_layout()
    plt.savefig("images/revenue_by_gender.png")
    plt.show()

def plot_revenue_by_payment_method(payment_revenue):
    """Create a bar chart of revenue by payment method."""

    plt.figure(figsize=(8, 5))

    payment_revenue.plot(
        kind="bar",
        color=["gray", "black", "pink"]
    )

    plt.title("Revenue by Payment Method")
    plt.xlabel("Payment Method")
    plt.ylabel("Revenue")

    plt.tight_layout()
    plt.savefig("images/revenue_by_payment_method.png")
    plt.show()

def plot_revenue_by_month(month_revenue):
    """Create a bar chart of revenue by month."""

    plt.figure(figsize=(8, 5))

    month_revenue.plot(
        kind="bar",
        color=["gray", "pink", "black"]
    )

    plt.title("Revenue by Month")
    plt.xlabel("Month")
    plt.ylabel("Revenue")

    plt.tight_layout()
    plt.savefig("images/revenue_by_month.png")
    plt.show()

def plot_revenue_by_day(revenue_by_day):
    """Create a bar chart of revenue by day of week."""

    plt.figure(figsize=(8, 5))

    revenue_by_day.plot(
        kind="bar",
        color="gray"
    )

    plt.title("Revenue by Day of Week")
    plt.xlabel("Day of Week")
    plt.ylabel("Revenue")

    plt.tight_layout()
    plt.savefig("images/revenue_by_day.png")
    plt.show()

def plot_revenue_by_hour(hour_revenue):
    """Create a bar chart of revenue by hour."""

    plt.figure(figsize=(10, 5))

    hour_revenue.plot(
        kind="bar",
        color="gray"
    )

    plt.title("Revenue by Hour")
    plt.xlabel("Hour")
    plt.ylabel("Revenue")

    plt.tight_layout()
    plt.savefig("images/revenue_by_hour.png")
    plt.show()

def plot_rating_by_branch(branch_rating):
    """Create a bar chart of average rating by branch."""

    plt.figure(figsize=(8, 5))

    branch_rating.plot(
        kind="bar",
        color="mediumpurple"
    )

    plt.title("Average Rating by Branch")
    plt.xlabel("Branch")
    plt.ylabel("Average Rating")

    plt.tight_layout()
    plt.savefig("images/rating_by_branch.png")
    plt.show()

def plot_rating_by_product(product_rating):
    """Create a bar chart of average rating by product line."""

    plt.figure(figsize=(10, 6))

    product_rating.plot(
        kind="barh",
        color="gray"
    )

    plt.title("Average Rating by Product Line")
    plt.xlabel("Average Rating")
    plt.ylabel("Product Line")

    plt.tight_layout()
    plt.savefig("images/rating_by_product.png")
    plt.show()