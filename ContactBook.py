class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name 
        self.phone = phone
        self.email = email
        self.adddress = address

    def update(self,phone = None, email = None, address = None):
        if phone:
            self.phone = phone
        if email:
            self.email = email
        if address:
            self.adddress = address
        print(f"Updated details for {self.name}")

    def __str__(self):
        return(f"Name: {self.name}\n"
               f"Phone: {self.phone}\n"
               f"Email: {self.email}\n"
               f"Address: {self.adddress}\n")
    
class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print(f"Contact {name} already exists")
                return
        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)
        print(f"Added contact {name}")

    def update_contact(self, name, phone = None, email = None, address = None):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                contact.update(phone, email, address)
                return
        print(f"Contact name {name} not found. ")
            
    def search_contact(self,name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print("\nContact Found.")
                print(contact)
                return
        print(f"Contact {name} not found. ")

    def display_all(self):
        if not self.contacts:
            print("No contact to display. ")
        else:
            print("All contact: ")
            for contact in self.contacts:
                print("-" * 30)
                print(contact)

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(name)
                print(f"Contact {name} has been removed from the list.")
        print(f"Contact {name} not found.")

