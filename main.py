# import keyboard
from payment_system import *
from config import logger
import sys


def main():

    logger.info("Welcome to Payment System")
    payment_instance = PaymentSystem()

    while True:

        logger.info("Use 1 --> Add, 2 --> refund, 3 --> check balance, 4 --> check history, 5 --> quit)")

        try:
            case_value = int(input("Select the options: "))
        except Exception as e:
            logger.error(f"Invalid input: {e}")
            sys.exit(0)

        try:
            match case_value:
                case 1:
                    try:
                        amount = int(input("Enter amount to credit: "))
                    except Exception as e:
                        logger.warning(f"Invalid amount input: {e}")

                        try:
                            amount = int(input("2nd time, Enter amount to credit: "))
                        except Exception as e:
                            logger.error(f"Failed to get valid amount: {e}")
                            break
                    try:
                        type = int(input("Enter the option (1: Card 2: UPI): "))
                    except Exception as e:
                        logger.warning(f"Invalid payment type input: {e}")
                        try:
                            type = int(input("2nd time, Enter the option (1: Card 2: UPI): "))
                        except Exception as e:
                            logger.error(f"Failed to get valid payment type: {e}")
                            break

                    payment_instance.credit_type(type, amount)

                case 2:
                    try:
                        refund_amount = int(input("Enter refund amount: "))
                    except Exception as e:
                        logger.warning(f"Invalid refund amount input: {e}")
                        try:
                            refund_amount = int(input("2nd Time , Enter refund amount: "))
                        except Exception as e:
                            logger.error(f"Failed to get valid refund amount: {e}")
                            break
                    
                    payment_instance.refund(refund_amount)

                case 3:
                    payment_instance.show_balanace()

                case 4:
                    payment_instance.check_history()

                case 5:
                    logger.info("Exiting...")
                    break
        except Exception as e:
            logger.error(f"Invalid option selected: {e}")


if __name__ == "__main__":
    main()