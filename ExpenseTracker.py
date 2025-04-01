
class Expense:
    def __init__(self, amount, category, date = None):
        self.amount = float(amount)
        self.category = category.lower()
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
            total = self.total_spending()
            if total > self.budget_limit:
                print(f"Warning! total spendings {total:.2f} exceeds budget limit {self.budget_limit:.2f}!")
            else:
                print(f"Total spending {total:.2f}. Remaining budget {self.budget_limit - total:.2f}")
