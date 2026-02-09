
from config import logger

class PaymentByUPI:
    def __init__(self):
        self.__amount = 0
    
    def credit_money(self, amount):
        logger.info(f"Depositing money by UPI: {amount}")

        self.__amount += amount
        return self.__amount