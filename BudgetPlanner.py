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
        valid_type = ["income", "expense"]
        if type.lower() not in valid_type():
            print(f"Invalid type! use: {', ' .join(valid_type)}")
            return
        
        new_transaction = Transaction(amount, type, category, date)
        self.transactions.append(new_transaction)
        print(f"Added transaction: {new_transaction}")
        self.check_budget()
        try:
            amount = float(amount)
            if amount <= 0:
                print("Invalid amount. Amount must be a positive number")
        except ValueError:
            print("Invalid Value. Please Enter a number")

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