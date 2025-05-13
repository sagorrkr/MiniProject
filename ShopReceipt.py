# Shop Management System for managing inventory, sales, and receipts

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
        self.sales = []  

    def add_item(self, name, price, stock):
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

        for index, quantity in selections:
            try:
                index = int(index) - 1
                quantity = int(quantity)
                if index < 0 or index >= len(self.items) or quantity <= 0:
                    print("Invalid item index or quantity.")
                    return None
            except ValueError:
                print("Invalid input. Use numbers for index and quantity.")
                return None
            item = self.items[index]
            if not item.reduce_stock(quantity):
                print(f"Not enough stock for {item.name} (Available: {item.stock}).")
                return None
            cost = item.price * quantity
            total += cost
            items_purchased.append((item, quantity, cost))
        timestamp = datetime.now()
        transaction_id = timestamp.strftime("%Y%m%d_%H%M%S")  # Changed: Use timestamp
        self.sales.append((items_purchased, total, timestamp, transaction_id))
        return items_purchased, total, timestamp, transaction_id

    def generate_receipt(self, items_purchased, total, timestamp, transaction_id):
        filename = f"receipt_{transaction_id}.txt"
        with open(filename, 'w') as f:
            f.write(f"Shop Receipt - Transaction ID: {transaction_id}\n")
            f.write(f"Date: {timestamp.strftime('%d-%m-%Y %H:%M:%S')}\n")
            f.write("=" * 50 + "\n")
            f.write(f"{'Item':<20} {'Qty':<8} {'Price':<10} {'Total':<10}\n")
            f.write("-" * 50 + "\n")