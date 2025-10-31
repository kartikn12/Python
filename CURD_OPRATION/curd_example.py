import mysql.connector # type: ignore

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="kartik",
    database="mydb20"

)

mycursor = mydb.cursor()

while True:
    menu="""
    press 1 for Insert
    press 2 for update
    press 3 for del
    press 4 for fetch
    press 5 exit
"""
    print(menu)
    ch=int(input("Enter "))

    if ch==1:
        name=input("name:")
        email=input("email")
        mob=int(input("mob"))
        query="insert into signup(name,email,mob) values('%s','%s','%s')"
        args=(name,email,mob)
        mycursor.execute(query % args)
        mydb.commit()
        print("Data print")

    elif ch==2:
        id=int(input("enter id"))
        name=input("name:")
        email=input("email")
        mob=int(input("mob"))
        query="update signup set name='%s',email='%s',mob='%s' where id='%s'"
        args=(name,email,mob,id)
        mycursor.execute(query%args)
        mydb.commit()
        print("Update done")

    elif ch==3:                     
        id=int(input("enter id:"))
        query="delete from signup where id='%s' "
        args=id
        mycursor.execute(query%args)
        mydb.commit()
        print("Removed")

    elif ch==4:
        query="select * from signup"
        mycursor.execute(query)

        for i in mycursor.fetchall():
            print(i)
    
    elif ch == 4:
        break
    else:
        print("!!!!!")
        break