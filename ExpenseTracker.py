
class Expense:
    def __init__(self, amount, caategory, date = None):
        self.amount = float(amount)
        self.category = caategory.lower()
#        self.date = date if date else datetime.now().strftime("%Y-%M-%D")
        
    def __str__(self):
        return f" {self.date} - {self.category.capitalize()}: {self.amount:.2f} "

class ExpenseTracker:
    def __init__(self, budget_limit = None):
        self.expenses = []
        self.budget_limit = budget_limit

    def add_expense(self, amount, category, date = None):
        expense = Expense(amount, category, date)
        self.expense.append(expense)
        print(f"Added Expense: {expense}")
        
    def display_expense(self):
        if not self.expenses:
            print("No Expense to display. ")
        else:
            print("\nAll expense: ")
            for expense in self.expenses:
                print(expense)
