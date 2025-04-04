#a program to manage a grocery shopping list, allowing you to add items, 
#mark them as bought, and display the list.

class GroceryItem: 
    def __init__(self, name, quantity = 1):
        self.name = name
        self.quantity = quantity
        self.bought = False

    def mark_bought(self):
        self.bought = True
        print(f"{self.name} marked as bought. ")

    def __str__(self):
        status = "✓" if self.bought else "✗"
        return f"{status} {self.name} (Qty: {self.quantity})"

class GroceryList:
    def __init__(self):
        self.items = []

    def add_items(self, name, quantity = 1):
        for item in self.items:
            if item.name.lower() == name.lower() and not name.bought:
                item.quantity += quantity 
                print(f"Updated {name} quantity to {item.quantity}")
                return
        new_item = GroceryItem(name, quantity)
        self.items.append(new_item)
        print(f"Added {name} (Qty: {quantity}) to the list. ")

    def mark_bought(self, name):
        for item in self.items:
            if item.name.lower() == name.lower():
                item.mark_bought()
                return
        print(f"{name} not found in the list. ")