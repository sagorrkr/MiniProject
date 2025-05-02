#managing medication schedules
from datetime import datetime, timedelta
class Medication:
    def __init__(self, name,  dosage, frequency, stock):
        self.name = name
        self.dosage = dosage 
        self.frequency = frequency.lower()
        self.stock = int(stock)
        self.last_taken = None

    def take_dose(self):
        now = datetime.now()
        today = now.date()
        if self.last_taken and self.last_taken.date() == today and self.frequency == "daily":
            print(f"{self.name} already taken today. ") 
            return