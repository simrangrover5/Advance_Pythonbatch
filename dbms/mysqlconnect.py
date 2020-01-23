import pymysql as sql

db = sql.connect(host="localhost",port=3306,user="root",password="",database = "batch11am")

c = db.cursor()

