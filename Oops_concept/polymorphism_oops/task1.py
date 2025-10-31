class User:
    def fun1(self):
        l=[1,2,3,1,2]
        l1=[]
        for i in l:
            if i not in l1:
                l1.append(i)
            
        print(l1)

class Customer(User):
    def fun1(self):
        super().fun1()
        print("method!")


obj=Customer()
obj.fun1()