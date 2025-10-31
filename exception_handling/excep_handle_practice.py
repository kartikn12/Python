try:
    n=int(input("Enter number 1:"))
    n1=int(input("Enter number 2:"))
    
    print("Divisin",n/n1)
    age = 15
    assert age >= 18, "Age must be 18 or above"

except ValueError as e:
    print(e)
    
except ZeroDivisionError as e:
    print(e)
    



