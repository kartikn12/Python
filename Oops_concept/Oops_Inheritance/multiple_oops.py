class P:
    def fun1(self):
        d1={'p':600,'q':300,'r':400}
        d2={'p':300,'q':200}    
        ans={}

        for i ,j in d1.items():
            for m,k in d2.items():
                if i==m:
                    ans[i]=j+k
        print(ans)
        print("P1 class")


class P1:
    def fun2(self):
        l=[3,4,5]
        l1=[12,45,63]
        d3={} 

        for i in range(len(l)):    
            d3[l[i]]=l1[i]
        print(d3)

        print("P2 class")

class C(P,P1):
    def fun3(self):
        print("C class")

obj=C()
obj.fun1()
obj.fun2()
obj.fun3()
    