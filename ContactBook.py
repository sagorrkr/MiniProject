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