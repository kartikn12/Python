n1 = int(input("Enter number: "))
n2 = int(input("Enter number: "))
n3 = int(input("Enter number: "))

if n1>n2 and n1>n3:
    print(n1,"is greatest")
    
elif n2>n1 and n2>n3:
    print(n2,"is greatest")

else:
    print(n3,"is greatest")