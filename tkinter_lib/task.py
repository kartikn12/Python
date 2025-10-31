from tkinter import *
from task1 import *
from task3 import *
from task2 import *
from task4 import *
from task5 import *


root=Tk()

root.geometry("500x500")
root.title("Registration From")

rname=Label(root,font=("Arial",12,"bold"),text="Registration from:")
rname.pack()     
name=Label(root,font=("Arial",12,"bold"),text="Enter Name:")
name.place(x=50,y=50)

email=Label(root,font=("Arial",12,"bold"),text="Enter Email:")
email.place(x=50,y=100)

mobile=Label(root,font=("Arial",12,"bold"),text="Enter mobile:")
mobile.place(x=50,y=150)

password=Label(root,font=("Arial",12,"bold"),text="Enter password:")
password.place(x=50,y=200)

cpassword =Label(root,font=("Arial",12,"bold"),text="Enter confirm pass:")
cpassword.place(x=50,y=250)

ename=Entry(root,width=25)
ename.place(x=270,y=60)


eemail=Entry(root,width=25)
eemail.place(x=270,y=110)


emobile=Entry(root,width=25)
emobile.place(x=270,y=160)


epassword=Entry(root,width=25)
epassword.place(x=270,y=210)


ecpassword=Entry(root,width=25)
ecpassword.place(x=270,y=260)

def insert_value():
        query="insert into signup(name,email,mobile,password,cpassword) values('%s','%s','%s','%s','%s')"
        args=(ename.get(),eemail.get(),emobile.get(),epassword.get(),ecpassword.get())
        mycursor.execute(query % args)
        mydb.commit()
        print("Data print")





insert=Button(root,text="Insert",font=("arial",18,"italic"),fg="red",command=insert_value)
insert.place(x=70,y=310)

update=Button(root,text="Update",font=("arial",18,"italic"),fg="red",command=update_value)
update.place(x=150,y=310)

delete=Button(root,text="Delete",font=("arial",18,"italic"),fg="red",command=delete_btn)
delete.place(x=250,y=310)

login_btn=Button(root,text="login",font=("arial",18,"italic"),fg="red",command=login)
login_btn.place(x=350,y=310)

serch=Button(root,text="search",font=("arial",18,"italic"),fg="red",command=search_value)
serch.place(x=250,y=400)
root.mainloop()

