#  //payment
class Payments:
    def __init__(self,customerName,amount,phoneNumber):
        self.customerName=customerName
        self.amount=amount
        self.phoneNumber=phoneNumber
    # adding customer names
    def input_customerName(self,new_customerName):
        return new_customerName
        #updating customers name in the payment 
    def update_customer(self, new_customerName):
        self.customer = new_customerName
        return new_customer
        #updating amounts in the payment list 
    def update_amount(self, new_amount):
        self.amount = new_amount
        return new_amount
        #updating phone Numbers in the payment list
    def update_phoneNumber(self, new_phoneNumber):
        self.phoneNumber= new_phoneNumber
        return new_phoneNumber
    def __str__(self):
       return f"{self.customerName}-{self.amount}-{self.phoneNumber}"

# //Payments
p2=Payments("Julius nyerere",1000,"07453233737")
print(p2)