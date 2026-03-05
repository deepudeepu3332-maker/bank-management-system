#Mainprogram
#view.py
import oracledb as orc
def view():
    try:
        con = orc.connect("system/DEEPIKA@localhost/orcl")
        cur = con.cursor()
        Acno = int(input("Enter customer number for view: "))
        cur.execute("""
            SELECT Acno, CusName, Pin, Balance
            FROM customer1
            WHERE Acno = :1
        """, (Acno,))
        record = cur.fetchone()

        print("-" * 40)
        if record:
            print(" Customer Found:")
            print(f"Acno Number : {record[0]}")
            print(f"Name           : {record[1]}")
            print(f"PIN            : {record[2]}")
            print(f"Balance        : {record[3]:.2f}")
        else:
            print(" Customer not found!")
        print("-" * 40)

    except orc.DatabaseError as db:
         error = db.args
         print("Problem in Oracle:", error.message)

    finally:

        if cur:
            cur.close()
        if con:
            con.close()

# Main program
view()

