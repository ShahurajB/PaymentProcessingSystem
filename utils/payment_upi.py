
from config import logger
from abstract_system import Payment

class PaymentByUPI(Payment):
    def __init__(self):
        self.__amount = 0
    
    def credit_money(self, amount):
        logger.info(f"Depositing money by UPI: {amount}")

        self.__amount += amount
        return self.__amount