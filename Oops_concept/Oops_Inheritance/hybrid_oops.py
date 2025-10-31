class A:
    def fun(self):
        n=65
        for i in range(1,6):
            for j in range(1,i+1):
                print(chr(n),end="")
            print()
        print("method A")

class B(A):
    def fun1(self):
        print("Method B")

class C:
    def fun2(self):
        print("Method C")

class D(C,B):
    def fun3(self):
        print("Method D")

obj=D()

obj.fun()
obj.fun1()
obj.fun2()
obj.fun3()