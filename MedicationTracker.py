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
        
    def is_due(self):
        if not self.last_taken:
            return True
        now = datetime.now()
        last = self.last_taken
        if self.frequency == "daily":
            return now.date() > last. date()
        elif self.frequency == "twice_daily":
            return (now - last).total_seconds() >= 12*3600
        return False
    
    def __str__(self):
        status = "Due" if self.is_due() else "Not Due"
        low_stock = " (Low stock!)" if self.stock <= 5 else ""
        last = self.last_taken.strftime("%d-%m-%Y %H:%M") if self.last_taken else "Never"
        return (f"Medication : {self.name} \n"
                f"Dosage: {self.dosage}, Frequency: {self.frequency.capitalize()} \n"
                f"Stock: {self.stock} doses {low_stock} \n"
                f"Status: {status}, Last taken: {last}"
        )