try:
    l=[23,4,56,7,88,12]

    n1=int(input("Enter number"))

    print("Value of index",l[n1])

except ValueError as e:
    print(e)
    
except IndexError as e:
    print(e)


#handle any kind of error for that we use only except     
except Exception as e:
    print(e)
    print("Invalid input")