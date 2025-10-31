def reverse():
    n=int(input("NUM: "))
    rem=0
    rev=0
    while(n!=0):
        rem=n%10
        rev=rev*10+rem
        n=n//10
    print(rev)

def prime():
    n=int(input("num: "))
    prime=0
    for i in range(1,n):
        if n%i==0:
            prime+=1
    if prime==2:
        print("prime!!")
    else:
        print("not prime")
        
def pattern():
    for i in range(1,6):
        print("*"*i)
def fibonnaci():
    n = int(input("Enter num:"))
    n1=0
    n2=1
    print(n1)
    print(n2)
    
    for i in range(3,n+1):
        n3=n1+n2
        print(n3)
        n1=n2
        n2=n3

while True:
    
    menu="""
    ????
    """
    print(menu)
    c=int(input("NUMBER: "))
    
    if c==1:
        reverse()
    elif c==2:
        prime()
    elif c==3:
        pattern()
    elif c==4:
        fibonnaci()
    elif c==5:
        print("!!!!!!!!")
    else:
        print("Invalid")
