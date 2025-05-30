#managing personal finances
from datetime import datetime

class Transaction:
    def __init__(self, amount, type, category, date=None):
        self.amount = float(amount)  
        self.type = type.lower()  
        self.category = category.lower()  
        self.date = date if date else datetime.now().strftime("%d-%m-%Y") 

    def __str__(self):
        return f"{self.date} - {self.type.capitalize()} ({self.category.capitalize()}): ${self.amount:.2f}"

class BudgetPlanner:
    def __init__(self, budget_limit):
        self.transactions = []
        self.budget_limit = float(budget_limit)

    def add_transaction(self, amount, type, category,date = None):
        valid_types = ["income", "expense"]
        if type.lower() not in valid_types:
            print(f"Invalid type! Use: {', '.join(valid_types)}.")
            return
        new_transaction = Transaction(amount, type, category, date)
        self.transactions.append(new_transaction)
        print(f"Added transaction: {new_transaction}")
        self.check_budget()
        try:
            amount = float(amount)
            if amount <= 0:
                print("Invalid amount. Amount must be a positive number")
                return
        except ValueError:
            print("Invalid Value. Please Enter a number")
            return

    def calculate_balance(self):
        income = sum(t.amount for t in self.transactions if t.type == "income")
        expenses = sum(t.amount for t in self.transactions if t.type == "expense")
        return income - expenses

    def check_budget(self):
        expenses = sum(t.amount for t in self.transactions if t.type == "expense")
        if expenses > self.budget_limit:
            print(f"WARNING: Expenses (${expenses:.2f}) exceed budget limit (${self.budget_limit:.2f})!")
        else:
            print(f"Expenses: ${expenses:.2f}. Budget remaining: ${self.budget_limit - expenses:.2f}")

    def display_transactions(self):
        if not self.transactions:
            print("No transactions recorded.")
            return
        print("\nAll Transactions:")
        print("Income:")
        for t in self.transactions:
            if t.type == "income":
                print(t)

        print("Expenses:")
        for t in self.transactions:
            if t.type == "expense":
                print(t)
        print(f"Current Balance: ${self.calculate_balance():.2f}")

    def category_summary(self):
        if not self.transactions:
            print("No transactions to summarize.")
            return
        category_totals = {}
        for t in self.transactions:
            if t.type == "expense":
                category_totals[t.category] = category_totals.get(t.category, 0) + t.amount
        if not category_totals:
            print("No expenses to summarize.")
        else:
            print("\nExpense Summary by Category:")
            for category, total in category_totals.items():
                print(f"{category.capitalize()}: ${total:.2f}") 

def main():
    try:
        budget_limit = float(input("Enter your monthly budget limit: $"))
        planner = BudgetPlanner(budget_limit) 
    except ValueError:
        print("Invalid budget! Using $500 as default.")
        planner = BudgetPlanner(500) 

    while True:
        print("\nBudget Planner Menu:")
        print("1. Add a transaction")
        print("2. Display all transactions")
        print("3. Show expense summary by category")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            type = input("Enter type(Income/expense)")
            amount = input("Enter amount")
            category = input("Enter category(salary/groceries/cloths)")
            date = input("Enter date(DD-MM-YYYY) or press 'Enter' for today") or None
            planner.add_transaction(amount, type, category, date)

        elif choice == "2":
            planner.display_transactions()

        elif choice == "3":
            planner.category_summary()

        elif choice == "4":
            print("Goodbye! Final financial summary:")
            planner.display_transactions()
            planner.category_summary()
            break
        else:
            print("Invalid choice. Please try again(1-4)")

if __name__ == "__main__":
    main()
    