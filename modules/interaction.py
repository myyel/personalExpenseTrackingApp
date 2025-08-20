import pandas as pd
from datetime import datetime


def get_user_input():
    try:
        date_str = input("Date (YYYY-MM-DD): ")
        date = datetime.strptime(date_str, "%Y-%m-%d")

        category = input("Category: ")
        amount = float(input("Amount ($): "))

        return {"Date": date.strftime("%Y-%m-%d"), "Category": category, "Amount": amount}
    except Exception as e:
        print("⚠️ Incorrect Entry:", e)
        return None


def add_expense(filepath):
    new_entry = get_user_input()
    if new_entry:
        df = pd.read_csv(filepath)
        df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
        df.to_csv(filepath, index=False)
        print("✅ Record Added.")


def view_expenses(filepath):
    df = pd.read_csv(filepath)
    print(df.to_string(index=True))  # index, it shows line number for user


def delete_expense(filepath):
    df = pd.read_csv(filepath)
    view_expenses(filepath)

    try:
        idx = int(input("The Line Number that you want to delete: "))
        if 0 <= idx < len(df):
            df = df.drop(index=idx).reset_index(drop=True)
            df.to_csv(filepath, index=False)
            print("🗑️ Record deleted.")
        else:
            print("❌ Invalid index.")
    except ValueError:
        print("❌ You should write a number.")


def update_expense(filepath):
    df = pd.read_csv(filepath)
    view_expenses(filepath)

    try:
        idx = int(input("The Line Number that you want to update: "))
        if 0 <= idx < len(df):
            print("Write new data (if it's empty, previous values are saved):")
            old = df.loc[idx]

            new_date = input(f"Date [{old['Date']}]: ") or old['Date']
            new_cat = input(f"Category [{old['Category']}]: ") or old['Category']
            new_amt = input(f"Amount [{old['Amount']}]: ") or str(old['Amount'])

            df.at[idx, 'Date'] = new_date
            df.at[idx, 'Category'] = new_cat
            df.at[idx, 'Amount'] = float(new_amt)

            df.to_csv(filepath, index=False)
            print("✏️ Record updated.")
        else:
            print("❌ Invalid index.")
    except ValueError:
        print("❌ You should write a number.")
