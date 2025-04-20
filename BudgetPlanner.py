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

