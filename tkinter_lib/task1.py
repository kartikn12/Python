from tkinter import *
# from task3 import *
def login():
    root=Tk()

    root.geometry("500x500")
    root.title("Login From")


    email=Label(root,font=("Arial",12,"bold"),text="Enter Email:")
    email.place(x=50,y=100)

    password=Label(root,font=("Arial",12,"bold"),text="Enter password:")
    password.place(x=50,y=200)


    eemail=Entry(root,width=25)
    eemail.place(x=270,y=110)
    # e_eemail=eemail.get()

    epassword=Entry(root,width=25)
    epassword.place(x=270,y=210)
    # e_epassword=epassword.get()

    submit=Button(root,text="submit",font=("arial",18,"italic"),fg="red")
    submit.place(x=250,y=310)
    
    root.mainloop()

