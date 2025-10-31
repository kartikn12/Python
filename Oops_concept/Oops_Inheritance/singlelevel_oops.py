class P:
    def fun1(self):
        for i in range(1,6):
            for j in range(1,i+1):
                print("*",end="")
            print()


class C(P):
    
    def fun2(self):
       

        s=input("enter:").lower() 
        s1=s[::-1]

        if s==s1:
            print("Palimdrom")
        else:
            print("OOOO")


obj=C()
obj.fun1()
obj.fun2()
