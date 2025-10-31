class Pattern:
    def fun(self):
        
        for i in range(1,6):
            for j in range(1,i+1):
                print("*",end="")
            print()

class Fact:
    def fun1(self):
        fac=1
        n=int(input("Enter number"))

        for i in range(1,n+1):
            fac=fac*i
        print(fac)  

class Str:

    def rev(self):

        s=input("enter:").lower() 
        s1=s[::-1]

        if s==s1:
            print("Palimdrom")
        else:
            print("OOOO")

class Fibo:
    def Num(self):
        n=0
        n1=1
        number=int(input("Enter number"))

        print(n)
        print(n1)

        for i in range(3,number+1):
            n3=n+n1
            print(n3)
            n=n1
            n1=n3
