# BankMainproject.py
import os
print("Current working directory:", os.getcwd())
from open_account import open_account
from delete_acc import delete_acc
from withdraw import with_draw
from deposit import deposit
from view import view
from viewall import viewall
from search import search
from pin_generate import pin_generate
from pin_update import pin_update


def main():
    while True:
        try:
            print("_" * 60)
            print("\t\tBANK MANAGEMENT SYSTEM")
            print("_" * 60)
            print("""
            1. Open Account
            2. Delete Account
            3. Withdraw
            4. Deposit
            5. View Single Account
            6. View All Accounts
            7. Search Account
            8. Generate PIN
            9. Update PIN
            10. Exit
            """)
            print("_" * 60)
            ch = int(input("Enter your choice (1–10): "))

            match ch:
                case 1:
                    open_account()
                case 2:
                    delete_acc()
                case 3:
                    with_draw()
                case 4:
                    deposit()
                case 5:
                    view()
                case 6:
                    viewall()
                case 7:
                    search()
                case 8:
                    pin_generate()
                case 9:
                    pin_update()
                case 10:
                    print("Thank you for using the bank system!")
                    break
                case _:
                    print("\t Invalid choice! Try again.")
        except ValueError:
            print("Please enter numbers only (1–10). Try again!")
#main program
if __name__ == "__main__":
 main()
