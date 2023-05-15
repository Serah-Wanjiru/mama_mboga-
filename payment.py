#  //payment
class Payments:
    def __init__(self,customer,amount,phoneNumber):
        self.customer=customer
        self.amount=amount
        self.phoneNumber=phoneNumber
    def update_customer(self, new_customer):
        self.customer = new_customer
    def update_amount(self, new_amount):
        self.amount = new_amount
    def update_phoneNumber(self, new_phoneNumber):
        self.phoneNumber= new_phoneNumber
    def __str__(self):
       return f"{self.customer}-{self.amount}-{self.phoneNumber}"

# //Payments
p2=Payments("Julius nyerere",1000,"07453233737")
print(p2)