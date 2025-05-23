# Shop Management System: An OOP example for managing inventory, sales, and receipts

from datetime import datetime
import os

class Item:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = float(price)
        self.stock = int(stock)

    def reduce_stock(self, quantity):
        if quantity > self.stock:
            return False
        self.stock -= quantity
        return True

    def __str__(self):
        return f"{self.name}: ${self.price:.2f} (Stock: {self.stock})"

class Shop:
    def __init__(self):
        self.items = []
        self.sales = []  # List of (items_purchased, total, timestamp, transaction_id)

    def add_item(self, name, price, stock):
        if not name.strip():
            print("Item name cannot be empty.")
            return
        for item in self.items:
            if item.name.lower() == name.lower():
                print(f"Item '{name}' already exists.")
                return
        try:
            price = float(price)
            stock = int(stock)
            if price < 0 or stock < 0:
                print("Price and stock must be non-negative.")
                return
        except ValueError:
            print("Invalid price or stock. Please enter numbers.")
            return
        new_item = Item(name, price, stock)
        self.items.append(new_item)
        print(f"Added item: {name}.")

    def display_items(self):
        if not self.items:
            print("No items in inventory.")
            return
        print(f"\nAvailable Items ({len(self.items)}):")
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item}")

    def process_purchase(self, selections):
        if not self.items:
            print("No items available for purchase.")
            return None
        items_purchased = []
        total = 0.0
        temp_selections = []
        for index, quantity in selections:
            try:
                index = int(index) - 1
                quantity = int(quantity)
                if index < 0 or index >= len(self.items) or quantity <= 0:
                    print("Invalid item index or quantity.")
                    return None
                item = self.items[index]
                if quantity > item.stock:
                    print(f"Not enough stock for {item.name} (Available: {item.stock}).")
                    return None
                temp_selections.append((item, quantity))
            except ValueError:
                print("Invalid input. Use numbers for index and quantity.")
                return None
        for item, quantity in temp_selections:
            item.reduce_stock(quantity)
            cost = item.price * quantity
            items_purchased.append((item.name, quantity, cost, item.price))
            total += cost
        timestamp = datetime.now()
        transaction_id = timestamp.strftime("%Y%m%d_%H%M%S")

        base_filename = f"receipt_{transaction_id}"
        filename = f"{base_filename}.txt"
        counter = 1
        while os.path.exists(filename):
            filename = f"{base_filename}_{counter}.txt"
            counter += 1
        self.sales.append((items_purchased, total, timestamp, transaction_id))
        return items_purchased, total, timestamp, transaction_id, filename

    def generate_receipt(self, items_purchased, total, timestamp, transaction_id, filename):
        with open(filename, 'w') as f:
            f.write(f"Shop Receipt - Transaction ID: {transaction_id}\n")
            f.write(f"Date: {timestamp.strftime('%d-%m-%Y %H:%M:%S')}\n")
            f.write("=" * 50 + "\n")
            f.write(f"{'Item':<20} {'Qty':<8} {'Price':<10} {'Total':<10}\n")
            f.write("-" * 50 + "\n")
            for item_name, quantity, cost, price in items_purchased:
                f.write(f"{item_name:<20} {quantity:<8} ${price:<9.2f} ${cost:.2f}\n")
            f.write("-" * 50 + "\n")
            f.write(f"Grand Total: ${total:.2f}\n")
            f.write("=" * 50 + "\n")
            f.write("Thank you for shopping with us!\n")
        print(f"Receipt generated: {filename}")
        return filename

    def display_sales_history(self):
        if not self.sales:
            print("No sales recorded.")
            return
        print(f"\nSales History ({len(self.sales)} transactions):")
        for items_purchased, total, timestamp, transaction_id in self.sales:
            print("-" * 50)
            print(f"Transaction ID: {transaction_id}")
            print(f"Date: {timestamp.strftime('%d-%m-%Y %H:%M:%S')}")
            print(f"Items Purchased:")
            for item_name, quantity, cost, price in items_purchased:
                print(f"  {item_name}: {quantity} x ${price:.2f} = ${cost:.2f}")
            print(f"Total: ${total:.2f}")

def main():
    shop = Shop()

    while True:
        print("\nShop Management System Menu:")
        print("1. Add item to inventory")
        print("2. Display inventory")
        print("3. Make a purchase")
        print("4. View sales history")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()
        if not choice:
            print("Choice cannot be empty. Please try again (1-5).")
            continue

        if choice == "1":
            name = input("Enter item name (e.g., Laptop): ").strip()
            if not name:
                print("Item name cannot be empty.")
                continue
            price = input("Enter price (e.g., 10.99): ").strip()
            if not price:
                print("Price cannot be empty.")
                continue
            stock = input("Enter stock quantity (e.g., 10): ").strip()
            if not stock:
                print("Stock cannot be empty.")
                continue
            shop.add_item(name, price, stock)

        elif choice == "2":
            shop.display_items()

        elif choice == "3":
            shop.display_items()
            print("\nEnter items to purchase (enter 'done' when finished):")
            selections = []
            while True:
                index = input("Enter item number (1, 2, etc.) or 'done': ").strip()
                if index.lower() == 'done':
                    break
                if not index:
                    print("Item number cannot be empty.")
                    continue
                quantity = input("Enter quantity (e.g., 2): ").strip()
                if not quantity:
                    print("Quantity cannot be empty.")
                    continue
                selections.append((index, quantity))
            if selections:
                result = shop.process_purchase(selections)
                if result:
                    items_purchased, total, timestamp, transaction_id, filename = result
                    shop.generate_receipt(items_purchased, total, timestamp, transaction_id, filename)
                else:
                    print("Purchase failed. Please try again.")
            else:
                print("No items selected for purchase.")

        elif choice == "4":
            shop.display_sales_history()

        elif choice == "5":
            confirm = input("Are you sure you want to exit? (yes/no): ").strip().lower()
            if confirm == 'yes':
                print("Goodbye! Final inventory:")
                shop.display_items()
                break
            else:
                print("Exit cancelled.")

        else:
            print("Invalid choice. Please try again (1-5).")

if __name__ == "__main__":
    main()