#left-side
# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()
    
# for i in range(1,6):
#     print("*" * i)
    
    
    
#right-side:
for i in range(1,6):
    for j in range(1,6-i):
        print(" ",end="")
    for k in range(1,i+1):
        print(" *",end="")
    print()

# for i in range(1,6):
#     print(" "*(6-i),"*"*i)

#reverse side
for i in range(5,0,-1):
    for j in range(1,6-i):
        print(" ",end="")
    for k in range(1,i+1):
        print(" *",end="")
    print()