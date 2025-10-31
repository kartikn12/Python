class A:
    def fun(self):
        print("P Class")


class B(A):
    def fun1(self):
        print("C1 Class")

class C(A):
    def fun2(self):
        print("C2 class")


obj=B()
obj.fun()
obj.fun1()



obj1=C()
obj1.fun()
obj1.fun2()