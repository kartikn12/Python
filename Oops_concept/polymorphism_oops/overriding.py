"""
polymorphism 

poly many

morphism froms
many from

method:

1,overloding-not support in py
2.overriding-inheritad class

"""


class A:
    def fun1(self):
        super().fun1()
        print("method 1")

class B:
    def fun1(self):
        print("method 2")

class C(A,B):#first argument use a for there we use super method in a because a & b has not relation in class
    #super method use for not override the method
    
    def fun1(self):
        super().fun1()
        print("method 3")

obj=C()
obj.fun1()