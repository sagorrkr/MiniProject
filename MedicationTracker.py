#managing medication schedules
from datetime import datetime, timedelta
class Medication:
    def __init__(self, name,  dosage, frequency, stock):
        self.name = name
        self.dosage = dosage 
        self.frequency = frequency.lower()
        self.stock = int(stock)




