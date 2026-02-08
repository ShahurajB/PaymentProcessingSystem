
class PaymentByCard:
    def __init__(self):
        self.__amount = 0
    
    def credit_money(self, amount):
        print(f"Deposit the money by credit card : {amount}")

        self.__amount += amount
        return self.__amount