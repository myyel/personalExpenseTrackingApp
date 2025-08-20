import matplotlib.pyplot as plt


def plot_expenses(df):
    # pie chart by category
    category_summary = df.groupby("Category")["Amount"].sum()

    plt.figure(figsize=(8, 6))
    category_summary.plot(kind='pie', autopct='%1.1f%%', startangle=140)
    plt.title("Category-Based Expense Distribution")
    plt.ylabel("")
    plt.tight_layout()
    plt.show()

    # Monthly Expense Changing
    df["Month"] = df["Date"].dt.to_period("M")
    monthly_summary = df.groupby("Month")["Amount"].sum()

    plt.figure(figsize=(8, 5))
    monthly_summary.plot(kind="bar", color="skyblue")
    plt.title("Monthly Expense")
    plt.xlabel("Month")
    plt.ylabel("Total Amount ($)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
