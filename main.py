# import keyboard
from payment_system import *


def main():

    print("Welcome to Payment System", end="\n")
    payment_instance = PaymentSystem()

    while True:

        print("Use " \
        "1 --> Add, " \
        "2 --> refund, " \
        "3 --> check balance, " \
        "4 --> check history, " \
        "5 --> quit)")

        try:
            case_value = int(input("Select the options: "))
        except Exception as e:
            print(f"Please Select the options correct option : {e}")

        try:
            match case_value:
                case 1:
                    try:
                        amount = int(input("Enter amount to credit: "))
                    except Exception as e:
                        print(f"There is exception :{e}")

                        try:
                            amount = int(input("2nd time, Enter amount to credit: "))
                        except Exception as e:
                            print(f"There is exception :{e}")
                            break
                    try:
                        type = int(input("Enter the option (1: Card 2: UPI): "))
                    except Exception as e:
                        print(f"There is exception :{e}")
                        try:
                            type = int(input("2nd time, Enter the option (1: Card 2: UPI): "))
                        except Exception as e:
                            print(f"There is exception :{e}")
                            break

                    payment_instance.credit_type(type, amount)

                case 2:
                    try:
                        refund_amount = int(input("Enter refund amount: "))
                    except Exception as e:
                        print("There is exception : {e}")
                        try:
                            refund_amount = int(input("2nd Time , Enter refund amount: "))
                        except Exception as e:
                            print("There is exception : {e}")
                            break
                    
                    payment_instance.refund(refund_amount)

                case 3:
                    payment_instance.show_balanace()

                case 4:
                    payment_instance.check_history()

                case 5:
                    print("Exiting...")
                    break
        except Exception as e:
            print(f"Please select correct option : {e}")


if __name__ == "__main__":
    main()