class A:
    def fun1(self):
        temp=0
        l=[56,27,32,41,16]
        n=len(l)

        for i in range(n):
            for j in range(i+1,n):
             if l[i]>l[j]:
               temp=l[i]
               l[i]=l[j]
               l[j]=temp
            
        print(l)

class B(A):
   def fun1(self):
        super().fun1()
        l1=[56,27,32,41,34]
        n=len(l1)

        for i in range(n):
            min=i
            for j in range(i+1,n):
               if l1[j]<min:
                  min=j
        l1[i], l1[min] = l1[min], l1[i]

        print(l1)

class C:
   def fun1(self):
      super().fun1()
      l2=[2,5,4,6,1,3]

      m=l2[0]
      for i in l2:
         if i<m:
            m=i
      print(m)

class D(C,B):
   def fun1(self):
    super().fun1()
    s=input("Enter Name:")
    rev=""
    for i in s:
        rev=i+rev
    print(rev)
          
obj=D()
obj.fun1()
