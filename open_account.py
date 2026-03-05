#program for open an account
#open an account.py
import oracledb as orc
def open_account():
    while True:
        try:


            conobj = orc.connect("system/DEEPIKA@localhost/orcl")
            curobj = conobj.cursor()


            while True:
                Acno = input("Enter Account Number (6 digits): ")
                if Acno.isdigit() and len(Acno) == 6:
                    Acno = int(Acno)
                    break
                else:
                    print("Error: Account number must be 6 digits only. Please try again.")


            while True:
                Cusname = input("Enter Customer Name: ")
                if Cusname.replace(" ", "").isalpha():
                    break
                else:
                    print("Error: Name must contain only alphabets. Please try again.")


            while True:
                pin = input("Set 4-digit PIN: ")
                if pin.isdigit() and len(pin) == 4:
                    pin = int(pin)
                    break
                else:
                    print("Error: PIN must be 4 digits. Please try again.")


            while True:
                balance = input("Enter initial deposit amount: ")
                if balance.isdigit() and int(balance) > 0:
                    balance = int(balance)
                    break
                else:
                    print("Error: Initial deposit must be greater than 0. Please try again.")


            iq = "INSERT INTO customer1 VALUES (:1, :2, :3, :4)"
            curobj.execute(iq, (Acno, Cusname, pin, balance))
            conobj.commit()
            print("Record Inserted Successfully")

            curobj.close()
            conobj.close()

        except Exception as e:
            print("\tUnexpected Error:", e)
            print("----------------------------------")

        ch = input("Do you want to enter another customer? (yes/no): ")
        if ch.lower() == "no":
            print("Enter ur choice")
            break
#main program
open_account()








