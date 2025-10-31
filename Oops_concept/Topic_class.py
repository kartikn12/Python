class Myclass:

    def fun(self):
        for i in range(1,6):
            print("*"*i)
    def fun1(self):
        for i in range(1,6):
            print(" "*(6-i),"*"*i)
    def fun2(self):
        for i in range(1,6):
            print(" "*(6-i)," *"*i)

obj=Myclass()

obj.fun()
obj.fun1()
obj.fun2()