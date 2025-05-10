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
