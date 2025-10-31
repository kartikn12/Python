# from task import *

from task1 import *


# obj=Pattern()
# obj1=Fact()
# obj2=Str()
# obj3=Fibo()

menu="""
Press 1
press 2
press 3
press 4
"""
while True:


    print(menu)

    ch=int(input("enter num:"))

    if ch==1:
        obj.fun()
    elif ch==2:
        obj1.fun1()
    elif ch==3:
        obj2.rev()
    elif ch==4:
        obj3.Num()
    else:
        print("Thank you")
        break




    