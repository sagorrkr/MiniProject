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