"""
op_overloding

-dunder method - magical method

1.__init__
constructor

it is a special method that call itself
object created

1.default
2.parameterized
3. copy

__str__
return string 

__add__
addition method
"""


class User:

    def __init__(self,a,b):
        print("Constructor called")
        self.a=a
        self.b=b

    def __str__(self):
        return f"{self.a},{self.b}"
    
    def __add__(self,ob):
        x=self.a+ob.a
        y=self.b+ob.b

        return x,y

    def __mul__(self,obj):
        x=self.a*obj.a
        y=self.b*obj.b

        return x,y
    def __sub__(self,obj):
        x=self.a-obj.a
        y=self.b-obj.b
        return x,y    

    def __div__(self,obj):
        x=self.a/obj.a
        y=self.b/obj.b
        return x,y
obj=User(40,30)
print(obj)

obj1=User(30,20)
print(obj1)

print("Add called",obj+obj1)
print("Mul called",obj*obj1)
print("Sub called",obj-obj1)
print("div called",obj/obj1)

