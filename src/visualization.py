import matplotlib.pyplot as plt


def plot_revenue_by_branch(branch_revenue):
    """Create a bar chart of revenue by branch."""

    plt.figure(figsize=(8, 5))

    branch_revenue.plot(kind="bar", color="teal")

    plt.title("Revenue by Branch")
    plt.xlabel("Branch")
    plt.ylabel("Revenue")

    plt.tight_layout()
    plt.savefig("images/revenue_by_branch.png")
    plt.show()

def plot_revenue_by_product_line(product_line_revenue):
    """Create a bar chart of revenue by product line."""

    plt.figure(figsize=(10, 6))

    product_line_revenue.plot(kind="barh", color=["seagreen", "teal"])

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
        color="olive"
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
        color=["brown", "black", "maroon"]
    )

    plt.title("Revenue by Payment Method")
    plt.xlabel("Payment Method")
    plt.ylabel("Revenue")

    plt.tight_layout()
    plt.savefig("images/revenue_by_payment_method.png")
    plt.show()