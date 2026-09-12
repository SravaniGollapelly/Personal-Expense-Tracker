from datetime import datetime


class Expense:
    def __init__(self, name, amount, category, date):
        self.name = name
        self.amount = amount
        self.category = category
        self.date = date


class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.filename = "expenses.txt"
        self.load_expenses()

    def add_expense(self, name, amount, category):
        date = datetime.now().strftime("%d-%m-%Y")

        expense = Expense(name, amount, category, date)
        self.expenses.append(expense)

        self.save_expenses()

        print("Expense added successfully.")

    def view_expenses(self):
        if len(self.expenses) == 0:
            print("No expenses found.")
            return

        print("\n----- Expense List -----")

        for i in range(len(self.expenses)):
            expense = self.expenses[i]

            print(
                i + 1,
                ".",
                expense.name,
                "- Rs.", expense.amount,
                "-",
                expense.category,
                "-",
                expense.date
            )

    def calculate_total(self):
        total = 0

        for i in range(len(self.expenses)):
            total = total + self.expenses[i].amount

        print("\nTotal Expense = Rs.", total)

    def search_expense(self, name):
        found = False

        for i in range(len(self.expenses)):
            expense = self.expenses[i]

            if expense.name.lower() == name.lower():
                print("\nExpense Found:")
                print("Name:", expense.name)
                print("Amount: Rs.", expense.amount)
                print("Category:", expense.category)
                print("Date:", expense.date)

                found = True

        if found == False:
            print("Expense not found.")

    def delete_expense(self, number):
        if number < 1 or number > len(self.expenses):
            print("Invalid expense number.")
            return

        deleted_expense = self.expenses[number - 1]

        self.expenses.pop(number - 1)
        self.save_expenses()

        print(
            deleted_expense.name,
            "has been deleted successfully."
        )

    def category_summary(self):
        if len(self.expenses) == 0:
            print("No expenses found.")
            return

        summary = {}

        for i in range(len(self.expenses)):
            expense = self.expenses[i]
            category = expense.category

            if category in summary:
                summary[category] = summary[category] + expense.amount
            else:
                summary[category] = expense.amount

        print("\n----- Category-wise Summary -----")

        categories = list(summary.keys())

        for i in range(len(categories)):
            category = categories[i]
            print(category, "=", "Rs.", summary[category])

    def save_expenses(self):
        with open(self.filename, "w") as file:
            for i in range(len(self.expenses)):
                expense = self.expenses[i]

                file.write(
                    expense.name + "," +
                    str(expense.amount) + "," +
                    expense.category + "," +
                    expense.date + "\n"
                )

    def load_expenses(self):
        try:
            with open(self.filename, "r") as file:
                lines = file.readlines()

                for i in range(len(lines)):
                    data = lines[i].strip().split(",")

                    if len(data) == 4:
                        name = data[0]
                        amount = float(data[1])
                        category = data[2]
                        date = data[3]

                        expense = Expense(
                            name,
                            amount,
                            category,
                            date
                        )

                        self.expenses.append(expense)

        except FileNotFoundError:
            pass


tracker = ExpenseTracker()


while True:
    print("\n===== PERSONAL EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total Expense")
    print("4. Search Expense")
    print("5. Delete Expense")
    print("6. Category-wise Summary")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter expense name: ")

        try:
            amount = float(input("Enter amount: "))

            if amount < 0:
                print("Amount cannot be negative.")
                continue

        except ValueError:
            print("Invalid amount. Please enter a number.")
            continue

        category = input("Enter category: ")

        tracker.add_expense(name, amount, category)

    elif choice == "2":
        tracker.view_expenses()

    elif choice == "3":
        tracker.calculate_total()

    elif choice == "4":
        name = input("Enter expense name to search: ")
        tracker.search_expense(name)

    elif choice == "5":
        tracker.view_expenses()

        if len(tracker.expenses) > 0:
            try:
                number = int(input("Enter expense number to delete: "))
                tracker.delete_expense(number)

            except ValueError:
                print("Invalid input. Please enter a number.")

    elif choice == "6":
        tracker.category_summary()

    elif choice == "7":
        print("Thank you for using Personal Expense Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")