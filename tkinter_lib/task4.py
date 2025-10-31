from tkinter import *
from task3 import *
def update_value():
    root=Tk()

    root.geometry("500x500")
    root.title("update From")

    id=Label(root,font=("Arial",12,"bold"),text="Enter id:")
    id.place(x=50,y=50)

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

    eid=Entry(root,width=25)
    eid.place(x=270,y=60)

    ename=Entry(root,width=25)
    ename.place(x=270,y=110)


    eemail=Entry(root,width=25)
    eemail.place(x=270,y=160)


    emobile=Entry(root,width=25)
    emobile.place(x=270,y=210)


    epassword=Entry(root,width=25)
    epassword.place(x=270,y=260)


    ecpassword=Entry(root,width=25)
    ecpassword.place(x=270,y=310)

    def update_btn():
        query="update signup set name='%s',email='%s',mobile='%s',password='%s',cpassword='%s' where id='%s'"
        args=(ename.get(),eemail.get(),emobile.get(),epassword.get(),ecpassword.get(),eid.get())
        mycursor.execute(query%args)
        mydb.commit()
        print("Update done")


    update=Button(root,text="update",font=("arial",18,"italic"),fg="red",command=update_btn)
    update.place(x=240,y=360)

    root.mainloop()