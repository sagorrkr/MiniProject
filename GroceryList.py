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

    def display_list(self):
        if not self.items:
            print("Your grocery list is empty. ")
            return
        else:
            print("\nGrocery List:")
            print('To buy')
            for item in self.items:
                if not item.bought:
                    print(item)
            print("Bought:")
            for item in self.items:
                if item.bought:
                    print(item)

    def clear_bought(self):
        self.items = [item for item in self.items if not item.bought]
        print("Cleared all the bought items from the list. ")

def main():
    grocery_list = GroceryList()

    while True:
        print("\nGrocery List Menu")
        print("\nGrocery List Menu:")
        print("1. Add an item")
        print("2. Mark an item as bought")
        print("3. Display list")
        print("4. Clear bought items")
        print("5. Exit")
    
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            name = input("Enter item name: ")
            try:
                quantity = int(input("Enter the quantity(Default 1)") or 1)
                grocery_list.add_items(name, quantity)
            except ValueError:
                print("Invalid Quantity. Using 1 insteead")
                grocery_list.add_items(name, 1)

        elif choice == "2":
            name = input("Enter the item name to mark bought: ")
            grocery_list.mark_bought(name)
        
        elif choice == "3":
            grocery_list.display_list()

        elif choice == "4":
            grocery_list.clear_bought()
        elif choice == "5":
            print("GoodBye! Here's your final list: ")
            grocery_list.display_list()
            break
        else:
            print("Invalid Input. Please try again(1-5)")
    
if __name__ == "__main__":
    main()