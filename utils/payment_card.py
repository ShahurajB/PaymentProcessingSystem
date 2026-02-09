
from config import logger
from abstract_system import Payment

class PaymentByCard(Payment):
    def __init__(self):
        self.__amount = 0
    
    def credit_money(self, amount):
        logger.info(f"Depositing money by credit card: {amount}")

        self.__amount += amount
        return self.__amount