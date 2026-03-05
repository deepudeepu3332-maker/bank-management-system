# deposit.py
import oracledb as orc
def deposit():
    try:
        conobj = orc.connect("system/DEEPIKA@localhost/orcl")
        curobj = conobj.cursor()

        Acno = int(input("Enter customer number for deposit: "))
        amount = float(input("Enter amount to deposit: "))
        print("-" * 40)
        dq = "UPDATE customer1 SET Balance = Balance + :1 WHERE Acno = :2"
        curobj.execute(dq, (amount, Acno))
        conobj.commit()

        if curobj.rowcount > 0:
            print(f" {amount} deposited successfully to account {Acno}")
        else:
            print(" Account number not found!")

        print("-" * 40)

    except orc.DatabaseError as db:
        error, = db.args
        print("Problem in Oracle:", error.message)
# Main program
deposit()
