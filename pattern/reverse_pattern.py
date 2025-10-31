for i in range(1,6):
    for k in range(1,7-i):
        print("*",end="")
    
    for j in range(1,i):
        print(" ",end="")
    print()

for i in range(5, 0, -1):
    print(" " * (5 - i) + "*" * i)



for i in range(5,0,-1):
    for k in range(1,6-i):
        print(" ",end="")
    
    for j in range(1,i+1):
        print("*",end="")
    print()
