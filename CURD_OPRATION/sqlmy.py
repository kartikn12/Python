import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="kartik"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS mydb20")
mydb.commit()

mydb=mysql.connector.connect(

    host="localhost",
    user="root",
    password="kartik",
    database="mydb20"
)
mycursor = mydb.cursor()
mycursor.execute("create table if not exists signup (id int primary key auto_increment," \
"name varchar(40)," \
"email varchar(40)," \
"mob bigint )")
print("done")
mydb.commit()
