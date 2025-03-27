#Inventory Management System

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Name: {self.name}, Price: ${self.price}, Quantity: {self.quantity}"
    
class Inventory:
    def __init__(self):
        self.products = []
    
    def add_products(self, product):
        self.products.append(product)
        print(f"{product} is added to the Inventory.")
    
    def remove_product(self, name):
        for product in self.products:
            if product.name.lower() == name.lower():
                self.products.remove(product)
                print(f"{name} is removed from the inventory.")
                return
            else:
                print(f"{name} not found in the inventory.")

    def update_quantity(self, name, new_quantity):
        for product in self.products:
            if product.name.lower() == name.lower():
                product.quantity = new_quantity
                print(f"Updated {name} quantity to {new_quantity}")
            else:
                (f"{name} not found in the inventory. ")

    def display_inventory(self):
        if not  self.products:
            print("Inventory is empty.")
        else:
            print("\nCurrent Inventory: ")
            for product in self.products:
                print(product)

    def total_value(self):
        total = sum(product.price * product.quantity for product in self.products)
        return total

if __name__ == "__main__":
    inventory = Inventory()

    inventory.add_products(Product("Laptop", 999, 3))
    inventory.add_products(Product("Smartphone", 600, 7))
    inventory.add_products(Product("Mouse", 20, 10))

    inventory.display_inventory()

    inventory.remove_product("mouse")
    inventory.update_quantity("Laptop", 10)

    inventory.display_inventory()

    print(f"Total inventory value: ${inventory.total_value():.2f}")

