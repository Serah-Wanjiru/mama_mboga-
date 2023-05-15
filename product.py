#Product class
class OurProducts:
    def __init__(self, name, price, quantity, description, category):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.description = description
        self.category = category
    def update_price(self, new_price):
        self.price = new_price
    def update_quantity(self, new_quantity, new_description):
        self.quantity = new_quantity
    def update_description(self, new_description):
        self.description = new_description
    def update_category(self, new_category):
        self.category = new_category
    def __str__(self):
        return f"{self.name} ,{self.price} ,{self.quantity} ,{self.description} , {self.category}"
p1 =OurProducts("Apple", 0.50, 100, "Fresh red apples", "Fruit")
    # //Product
print(p1)
