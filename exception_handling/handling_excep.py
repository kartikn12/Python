try:
    n=int(input("Enter number 1:"))
    n1=int(input("Enter number 2:"))

    print("Addtion:",n+n1)    
    
except ValueError as e:
    print(e)
    
else:
    print("Try executed")

finally:
    print("Finally executed!!")
   

 