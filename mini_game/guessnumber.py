import random

num=random.randint(1001,9999)
print(num)
l=[677,889,333,21,2344]

print(random.choice(l))

orignal=random.randint(1,50)

print("Enter number beetween 1 to 50")

while True:
    
    ch=int(input("Enter number:"))
    
    if ch>50:
        print("invalid")
        break
    elif orignal==ch:
        print("win!!")
    elif orignal<ch:
        print("Greater number")
    else:
        print("smaller number")

