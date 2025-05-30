from datetime import datetime
class Expense:
    def __init__(self, amount, category, date = None):
        self.amount = float(amount)
        self.category = category.lower()
        self.date = date if date else datetime.now().strftime("%Y-%M-%D")
        
    def __str__(self):
        return f" {self.date} - {self.category.capitalize()}: {self.amount:.2f} "

class ExpenseTracker:
    def __init__(self, budget_limit = None):
        self.expenses = []
        self.budget_limit = budget_limit

    def add_expense(self, amount, category, date = None):
        expense = Expense(amount, category, date)
        self.expenses.append(expense)
        print(f"Added Expense: {expense}")

    def display_expenses(self):
        if not self.expenses:
            print("No Expense to display. ")
        else:
            print("\nAll expense: ")
            for expense in self.expenses:
                print(expense)

    def total_by_category(self):
        if not self.expenses:
            print("No expense to show/summerize")
            return
        category_total = {}
        for expense in self.expenses:
            category_total[expense.category] = category_total.get(expense.category, 0) + expense.amount

        print("\nTotal spendings by category: ")
        for category , total in category_total.items():
            print(f"{category.capitalize()}: {total:.2f}")

    def total_expense(self):
        return sum(expense.amount for expense in self.expenses)
    
    def check_budget(self):
        if self.budget_limit:
            total = self.total_expense()
            if total > self.budget_limit:
                print(f"Warning! total spendings {total:.2f} exceeds budget limit {self.budget_limit:.2f}!")
            else:
                print(f"Total spending {total:.2f}. Remaining budget {self.budget_limit - total:.2f}")


def main():
    tracker = ExpenseTracker(budget_limit=100)

    while True:
        print("\nExpense Tracker Menu: ")
        print("1. Add an Expense. ")
        print("2. Display all expense. ")
        print("3. Show total spendings by category. ")
        print("4. Exit. ")

        choice = input("Enter your choice(1-4): ")

        if choice == "1":
            try:
                amount = float(input("Enter the expense amount: "))
                category = input("Enter category: ")
                date = input("Enter date(DD-MM-YYYY): ") or None
                tracker.add_expense(amount, category, date)

            except ValueError:
                print("Invalid Value. Please type a valid integer(1-4)")

        elif choice == "2":
            tracker.display_expenses()
        elif choice == "3":
            tracker.total_by_category()
        elif choice == "4":
            print("Goodbye! Here is your final summery. ")
            tracker.display_expenses()
            tracker.total_by_category()
            break
        else:
            print("Invalid input. Please try again (1-4)")

if __name__ == "__main__":
    main()

