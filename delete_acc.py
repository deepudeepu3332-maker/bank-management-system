import oracledb as orc
def delete_acc():
    try:
        # Step 1: Connect to Oracle
        con = orc.connect("system/DEEPIKA@localhost/orcl")
        cur = con.cursor()

        # Step 2: Ask for account number to delete
        Acno = int(input("Enter customer number to delete: "))

        # Step 3: Check if the record exists
        cur.execute("SELECT * FROM customer1 WHERE Acno = :1", (Acno,))
        record = cur.fetchone()

        if record:
            # Step 4: Confirm delete
            print("-" * 40)
            print(f"Account Number : {record[0]}")
            print(f"Customer Name  : {record[1]}")
            print(f"PIN            : {record[2]}")
            print(f"Balance        : {record[3]}")
            print("-" * 40)
            choice = input("Do you really want to delete this record? (yes/no): ").lower()

            if choice == "yes":
                cur.execute("DELETE FROM customer1 WHERE Acno = :1", (Acno,))
                con.commit()
                print(" Customer record deleted successfully!")
            else:
                print(" Deletion cancelled.")
        else:
            print(" Customer record not found!")

    except orc.DatabaseError as e:
        print("Problem in Oracle:", e)

    finally:
        if cur:
            cur.close()
        if con:
            con.close()

# Main program
delete_acc()
