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
        if self.stock <= 0:
            print(f"No stock left for {self.name}. Time to refill!")
            return

        self.stock -= 1
        self.last_taken = now
        print(f"Recorded dose of {self.name}. Stock left: {self.stock} doses.")
        