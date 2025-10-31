from tkinter import *
from tkinter import messagebox
from task3 import *

def delete_btn():

    root=Tk()

    root.geometry("300x300")
    root.title("delete From")

    name=Label(root,font=("Arial",12,"bold"),text="Enter id:")
    name.place(x=50,y=50)

    ename=Entry(root,width=25)
    ename.place(x=120,y=50)
    
    

    
    def delete_value():
        query="delete from signup where id='%s' "
        args=(ename.get(),)
        mycursor.execute(query%args)
        mydb.commit()
        if mycursor.rowcount > 0:
            messagebox.showinfo("Deleted", "Record Deleted Successfully!")
            # messagebox.OKCANCEL("delete","sdfghjk")
        else:
            messagebox.showwarning("Not Found", "No record found with this ID.")
        

    deletes=Button(root,text="Delete",font=("arial",18,"italic"),fg="red",command=delete_value)
    deletes.place(x=100,y=200)

    root.mainloop() 


# delete()