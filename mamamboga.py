#Customer class
class Customer:
    def __init__(self, name, email, phone_number, address, order_history):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.address = address
        self.order_history = order_history
    def update_email(self, new_email):
        self.email = new_email
        return new_email
    def update_phone_number(self, new_phone_number):
        self.phone_number = new_phone_number
        return new_phone_number
    def update_address(self, new_address):
        self.address = new_address
        return new_address
    def add_order_to_history(self, order):
        return self.order_history.append(order)

    def __str__(self):
        return f"{self.name},{self.email},{self.phone_number},{self.address},{self.order_history}"


#//Customer class
c1 = Customer("Eunice Musenyia", "eunicemusenyia@gmail.com", "555-1234", "123 Main vt.")
#//Customer
print(c1)