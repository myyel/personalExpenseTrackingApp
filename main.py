from modules.data_handler import generate_sample_data, load_data
from modules.analyzer import analyze_expenses
from modules.plotter import plot_expenses
from modules.interaction import add_expense, view_expenses, delete_expense, update_expense

DATA_PATH = "data/expenses.csv"


def main():
    # if a file doesn't exist, create sample data
    try:
        with open(DATA_PATH, "r") as f:
            pass
    except FileNotFoundError:
        generate_sample_data(DATA_PATH)

    while True:
        print("\n--- 📊 Personal Expense Tracking ---")
        print("1. Add New Expense")
        print("2. Show Expenses")
        print("3. Delete Expense")
        print("4. Update Expense")
        print("5. Analysis Expense")
        print("6. Show with Graphics")
        print("0. Exit")

        choice = input("Your choice: ")

        if choice == "1":
            add_expense(DATA_PATH)
        elif choice == "2":
            view_expenses(DATA_PATH)
        elif choice == "3":
            delete_expense(DATA_PATH)
        elif choice == "4":
            update_expense(DATA_PATH)
        elif choice == "5":
            df = load_data(DATA_PATH)
            analyze_expenses(df)
        elif choice == "6":
            df = load_data(DATA_PATH)
            plot_expenses(df)
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("❌ Invalid entry.")


if __name__ == "__main__":
    main()
