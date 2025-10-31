"""
encaps

data binding into single entity it called encaps

e.x: class

pointer:
store the address of next variable

example:

"""

class e():
    def fun1(self):
        a=10
        self.a=a        
    def fun2(self):
        print(self.a)

obj=e()
obj.fun1()
obj.fun2()