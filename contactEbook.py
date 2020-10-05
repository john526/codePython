
import sqlite3
"""
This is one of the excellent python projects for beginners.
Everyone uses a contact book to save contact details,
including name, address, phone number, and even email address.
This is a command-line project where you will design a contact book application
that users can use to save and find contact details. The application should also allow
users to update contact information, delete contacts, and list saved contacts.
The SQLite database is the ideal platform for saving contacts.



"""
#bd connection
db = sqlite3.connect("ebook.db")

def create():
    db.row_factory = sqlite3.Row
    # create table if not exists ...
    db.execute(""" 
        CREATE TABLE if not exists contact(id integer primary key autoincrement, name VAR(255), adress VAR(255), email VAR(255), phone VAR(255)) 
        """)
    db.commit()

def insertData(name,adress,email,phone):
    db.row_factory = sqlite3.Row
    db.execute("INSERT INTO contact(name,adress,email,phone) VALUES(?,?,?,?)",(name,adress,email,phone))
    db.commit()
    print("operation end")

def selectData():
    coursor = db.execute("SELECT * FROM contact")
    for row in coursor:
        print("ID : {} > Name : {} | adress : {} | email : {} | phone : {} ".format(row["id"],row["name"],row["adress"],row["email"],row["phone"]))

def deleteData(id):
    db.row_factory = sqlite3.Row
    db.execute("DELETE FROM contact WHERE name = '{}' ".format(id))
    db.commit()
    print("delete end")

def updateData(id,name):
    db.row_factory = sqlite3.Row
    db.execute("UPDATE contact SET id= ? WHERE name = ? ",(id,name))
    db.commit()
    print("update end")

def main(): # main function
    create()

    while 1 :
        indexOfOp = int(input("======================\nSelect operation : > 1-Add \n > 2-Select > \n 3-delete > \n 4-update \n 0-exit\n\n============ \n\n index :"))
        if indexOfOp == 0:
            break
        elif indexOfOp == 1:
            name = input("entrez name : > ")
            adress = input("entrez adress : > ")
            email = input("entrez email : > ")
            phone = input("entrez phone : > ")
            insertData(name,adress,email,phone)

        elif indexOfOp == 2:
            selectData()

        elif indexOfOp == 3:
            id = int(input("entrez id : > "))
            deleteData(id)

        elif indexOfOp == 4:
            id = int(input("entrez id : > "))
            name = input("entrez name : >")
            updateData(id,name)
        else:
            pass



if __name__ == "__main__":
    main()