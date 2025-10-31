from tkinter import *
from task3 import *
def search_value():
    root=Tk()

    root.geometry("500x500")
    root.title("search From")

    id=Label(root,font=("Arial",12,"bold"),text="Enter id:")
    id.place(x=50,y=50)
    eid=Entry(root,width=25)
    eid.place(x=270,y=60)


    name=Label(root,font=("Arial",12,"bold"),text="Enter Name:")
    name.place(x=50,y=100)

    email=Label(root,font=("Arial",12,"bold"),text="Enter Email:")
    email.place(x=50,y=150)

    mobile=Label(root,font=("Arial",12,"bold"),text="Enter mobile:")
    mobile.place(x=50,y=200)

    password=Label(root,font=("Arial",12,"bold"),text="Enter password:")
    password.place(x=50,y=250)

    cpassword =Label(root,font=("Arial",12,"bold"),text="Enter confirm pass:")
    cpassword.place(x=50,y=300)


   
    def serch_btn():
        query="select name,email,mobile,password,cpassword from signup where id ='%s'"
        args=(eid.get(),)
        mycursor.execute(query % args)
        row=mycursor.fetchone()

        if row:
            name.config(text=f"Name:{row[0]}")
            email.config(text=f"email:{row[1]}")
            mobile.config(text=f"mobile:{row[2]}")
            password.config(text=f"password:{row[3]}")
            cpassword.config(text=f"cpassword:{row[4]}")



    search=Button(root,text="search",font=("arial",18,"italic"),fg="red",command=serch_btn)
    search.place(x=240,y=360)

    root.mainloop()