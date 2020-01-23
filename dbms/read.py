import sqlite3 as sql

db = sql.connect("bank.db")
c = db.cursor()

cmd = "select * from customer"
c.execute(cmd)

data = c.fetchall()
print(data)
