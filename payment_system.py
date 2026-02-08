from utils import *
import time
import re

class PaymentSystem:

    def __init__(self):
        self.__amount = 0
        self.__history = []
        self.__payByCard = PaymentByCard()
        self.__payByUPI = PaymentByUPI()

    def credit_type(self, credit_type, amount):
    
        if 1 == credit_type:
            amnt = self.__payByCard.credit_money(amount)
            self.__amount += amnt
            t1 = time.time()
            self.__history.append(f'Transaction_{t1}: credited amount by card: {amount} balance: {self.__amount}')

        elif 2 == credit_type:
            amnt = self.__payByUPI.credit_money(amount)
            self.__amount += amnt
            t1 = time.time()
            self.__history.append(f'Transaction_{t1}: credited amount by upi: {amount} balance: {self.__amount}')
        else:
            print("Please provide correct type of payment")

    
    def refund(self, refund_amount):
        print(f"refund money: {refund_amount}")
        if refund_amount <= self.__amount:
            self.__amount -= refund_amount
            t1 = time.time()
            self.__history.append(f'Transaction_{t1}: refund amount: {refund_amount} balance: {self.__amount}')
        else:
            print("Insuffient balance in account: balance is: {self.__amount}")

    def show_balanace(self):
        print(f"Your balance is: {self.__amount}")

    def check_history(self):
        print("-" * 72)
        print(f"| {'TXN ID':<22} | {'TYPE':<10} | {'METHOD':<8} | {'AMOUNT':>8} | {'BALANCE':>8} |")
        print("-" * 72)

        for transactions in self.__history:
            pattern = r"Transaction_(.*?): (.*?) amount(?: by (.*?))?: (\d+) balance: (\d+)"
            match_obj = re.search(pattern, transactions)

            if match_obj:
                txn_id, action, method, amount, balance = match_obj.groups()

                if method:
                    method = method
                else:
                    method = "N/A"

                match action:
                    case "credited":
                        display_action = "CREDIT"
                        prefix = "+"
                    case "refund":
                        display_action = "REFUND"
                        prefix = "↺"

                print(f"| {txn_id:<22} | {display_action:<10} | {method.upper():<8} | {prefix}{amount:>7} | {balance:>8} |")
            
        print("-" * 72)
