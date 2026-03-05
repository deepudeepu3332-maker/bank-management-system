#program for generate the pin
#pin_generate.py
import oracledb as orc
def pin_generate():
        try:
            conobj = orc.connect("system/DEEPIKA@localhost/orcl")
            curobj = conobj.cursor()
            Acno = int(input("Enter customer Number for pin_generate: "))
            pin_generate = int(input("generate pin:"))
            print("-" * 40)
            # uq="update customer set pin=%f where Acno=%d"
            # curobj.execute(uq % (Acno,newpin))
            uq = "UPDATE customer SET pin = :0 WHERE Acno = :1"
            curobj.execute(uq, (pin_generate, Acno))
            conobj.commit()
            if (curobj.rowcount > 0):
                print("{} pin generated".format(curobj.rowcount))
            else:
                print("customer Number does not exist")
                print("-" * 40)

        except orc.DatabaseError as db:
                 print("Problem in Oracle: ", db)

# Main Program
#pin_generate()



