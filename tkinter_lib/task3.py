import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="kartik"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS user_data")
mydb.commit()

mydb=mysql.connector.connect(

    host="localhost",
    user="root",
    password="kartik",
    database="user_data"

)
mycursor = mydb.cursor()
mycursor.execute("create table if not exists signup (id int primary key auto_increment,name varchar(40),email varchar(40),mobile varchar(20),password varchar(20),cpassword varchar(20))"

)
print("done")
mydb.commit()