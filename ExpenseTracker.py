
class Expense:
    def __init__(self, amount, caategory, date = None):
        self.amount = float(amount)
        self.category = caategory.lower()
#        self.date = date if date else datetime.now().strftime("%Y-%M-%D")
        
    def __str__(self):
        return f" {self.date} - {self.category.capitalize()}: {self.amount:.2f} "