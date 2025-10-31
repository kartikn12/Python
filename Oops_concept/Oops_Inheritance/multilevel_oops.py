class A:
    def fun(self):

        # s=input("enter:").lower() 
        s="dvd"
        s1=s[::-1]

        if s==s1:
            print("Palimdrom")
        else:
            print("not")

    def fun1(self):
        fac=1
        # n=int(input("Num:"))
        n=5
        for i in range(1,n+1):
            fac = fac*i
        print(fac)
    
class B(A):
    def fun2(self):
        pr=0
        # n=int(input("Num:"))
        n=7
        for i in range(1,n+1):
            if n%i==0:
                pr+=1
        if pr==2:
            print("prime")
        else:
            print("not prime")

class C(B):
    def fun3(self):

        for i in range(1,6):
            for j in range(1,i+1):
                print("*",end="")
            print()


obj = C()
obj.fun()
obj.fun1()
obj.fun2()
obj.fun3()