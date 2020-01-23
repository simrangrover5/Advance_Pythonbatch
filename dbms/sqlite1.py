import sqlite3 as sql

db = sql.connect("bank.db")
c = db.cursor()

#cmd = "create table customer(id integer,name varchar(50),address varchar(100))"

#c.execute(cmd)
while True:
    id1 = int(input("Enter your id : "))
    name = input("Enter your name : ")
    address = input("Enter address : ")
    cmd = "insert into customer values({},'{}','{}')".format(id1,name,address)
    c.execute(cmd)
    db.commit()
    ch = input("Do you want to continue(y/n): ")
    if ch == "n":
        print("Thanks for coming")
        break
