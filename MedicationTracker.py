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
                f"Status: {status}, Last taken: {last}")
    
class MedicationTracker:
    def __init__(self):
        self.medications = []

    def add_medication(self, name, dosage, frequency, stock):
        valid_frequencies = ["daily", "twice_daily"]
        if frequency.lower() not in valid_frequencies:
            print(f"Invalid frequency. Use: {', '.join(valid_frequencies)}.")
            return
        for med in self.medications:
            if med.name.lower() == name.lower():
                print(f"Medication {name} already exist.")
                return  
        try:
            stock = int(stock)
            if stock < 0:
                print("Stock can't be negative.")
                return
        except ValueError:
            print("Invalid stock. Please enter a number.")
            return
        new_med = Medication(name, dosage, frequency, stock)
        self.medications.append(new_med)
        print(f"Added Medication: {name}")

    def take_dose(self, name):
        for med in self.medications:
            if med.name.lower() == name.lower():
                med.take_dose()
                return
        print(f"Medication {name} not found.")

    def display_medications(self):
        if not self.medications:
            print("No medication to display.")
            return
        for med in self.medications:
            print("-" * 30)
            print(med)

    def check_stocks(self):
        low_stock = [med for med in self.medications if med.stock < 5]
        if not low_stock:
            print("No medications are low on stock.")
        else: 
            print("\nLow stock warnings:")
            for med in med.low_stock:
                print(f"{med.name} : {med.dosage} dosage remaining")

def main():
    tracker = MedicationTracker()

    while True:
        print("\nMedication Tracker Menu:")
        print("1. Add a medication")
        print("2. Record a dose taken")
        print("3. Display all medications")
        print("4. Check low stock")
        print("5. Exit")

        choice =  input("Enter your choice(1-5):")
        if choice == "1":
            name = input("Enter medication name: ")
            dosage = input("Enter dosage (e.g., 1 pill): ")
            frequency = input("Enter frequency (daily/twice_daily): ")
            stock = input("Enter stock (number of doses): ")
            tracker.add_medication(name, dosage, frequency, stock)

        elif choice == "2":
            name = input("Enter medication name to record dose: ")
            tracker.take_dose(name)

        elif choice == "3":
            tracker.display_medications()

        elif choice == "4":
            tracker.check_stock()

        elif choice == "5":
            print("Goodbye! Final medication summary:")
            tracker.display_medications()
            break

        else:
            print("Invalid choice. Please try again (1-5).")

if __name__ == "__main__":
    main()
    