def analyze_expenses(df):
    print("🔍 Total Expense:", round(df["Amount"].sum(), 2), "$")

    print("\n📊 Category-Based Expense:")
    category_summary = df.groupby("Category")["Amount"].sum().sort_values(ascending=False)
    print(category_summary.to_string())

    print("\n📅 Monthly Expense:")
    df["Month"] = df["Date"].dt.to_period("M")
    monthly_summary = df.groupby("Month")["Amount"].sum()
    print(monthly_summary.to_string())
