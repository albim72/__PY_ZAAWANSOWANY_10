import mysql.connector

db = mysql.connector.connect(user='root',password='abc123',host='127.0.0.1',port=3306,database='mojabazadotestow')

cursorObject = db.cursor()
tabela_student = ("CREATE TABLE IF NOT EXISTS student(firstname varchar(100),"
                  "lastname varchar(100), nrstudenta int);")
cursorObject.execute(tabela_student)

ins_data = "INSERT INTO student(firstname,lastname,nrstudenta) values(%s,%s,%s);"
val_one = ("Jan","Kot",763656)
cursorObject.execute(ins_data,val_one)

val_multi = [
    ("Maria","Wasek",6554435),
    ("Ola","Kot",56767),
    ("Jan","Kos",655443),
    ("Marek","Kłos",6553434),
    ("Henryk","Nowak",654234),
    ("Nadia","Nowik",645455),
    ("Roch","Wac",655476435),
    ("Leon","Ryc",6554567),
]

cursorObject.executemany(ins_data,val_multi)
db.commit()
db.close()
