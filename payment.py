#  //payment
class Payments:
    def __init__(self,customer,amount,phoneNumber):
        self.customer=customer
        self.amount=amount
        self.phoneNumber=phoneNumber
        #updating customers name in the payment 
    def update_customer(self, new_customer):
        self.customer = new_customer
        #updating amounts in the payment list 
    def update_amount(self, new_amount):
        self.amount = new_amount
        #updating phone Numbers in the payment list
    def update_phoneNumber(self, new_phoneNumber):
        self.phoneNumber= new_phoneNumber
    def __str__(self):
       return f"{self.customer}-{self.amount}-{self.phoneNumber}"

# //Payments
p2=Payments("Julius nyerere",1000,"07453233737")
print(p2)