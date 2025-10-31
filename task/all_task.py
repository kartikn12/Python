class A:
    #FACTORIAL NUMBER
    def Fact(self):
        fac=1
        
        n=int(input("Enter num:"))
        for i in range(1,n+1):
            fac *=i

        print(fac)

    #REVERSE NUMBER
    def reverse(self):
        n=int(input("Enter num:"))
        rev=0
        rem=0
        while n!=0:
            rem=n%10
            print("rem:",rem)

            rev=rev*10+rem
            print("reverse",rev)
            n=n//10
            print("number",n)

    #PRIME NUMBER
    def pr(self):
        prime=0
        n=int(input("Enter num:"))

        for i in range(1,n+1):
            if n%i==0:
                prime+=1
        if prime==2:
            print("prime!!")
        else:
            print("Not!!")

    #LIST PALIMDROM wITHOUT BUIT-IN METHOD
    def pal(self):
        l=[1,2,3,2,1]

        left=0
        right=len(l)-1

        while left<right:
            if l[left] != l[right]:
                return "Not palimdrom"
            left+=1
            right-=1
        return "Palimdrom"
    
    #TWO-DICT ADDITION
    def dic(self):
        d={'p':200,'q':300,'r':900}
        d1={'p':300,'q':400}
        d2={}

        for i,j in d.items():
            for m,k in d1.items():
                if i==m:
                    d2[i]=j+k
        print(d2)

    #LIST MAX VALUE FIND
    def max(self):
        l=[23,45,67,43,2,1]
        m=l[0]
        for i in l:
            if i>m:
                m=i
        print(m)

    #MID POINT OF STRING
    def mid(self):
        s=input("enter name:")

        s1=len(s)//2

        if s1%2==0:
            return "enter vaild string"
        else:
            return s[s1-1]+s[s1]+s[s1+1]
        
    #REVERSE STRING
    def rev_str(self):
        s=input("Name:")
        rev=""

        for i in s:
            rev=i+rev
            print(rev)
    
    #STORE LIST INTO DICT
    def l_to_d(self):
        l=[3,4,5]
        l1=[12,45,63]
        d3={} 

        for i in range(len(l)):
            d3[l[i]]=l1[i]
        print(d3)
    
    #PATTERN-LEFT SIDE
    def pattern(self):

        for i in range(1,6):
            for j in range(1,i+1):
                print("*",end="")
            print()
        
        for i in range(1,6):
            print("*"*i)

    #PATTERN-RIGHT SIDE
    def pattern1(self):

        for i in range(1,6):
            for k in range(1,6-i):
                print(" ",end="")
            for j in range(1,i+1):
                print("*",end="")
            print()
        
        for i in range(1,6):
            print(" "*(6-i)," *"*i)

    
    #PATTERN-REVERSE SIDE
    def pattern2(self):

        for i in range(5,0,-1):
            for k in range(1,6-i):
                print(" ",end="")
            for j in range(1,i+1):
                print("*",end="")
            print()
        
        for i in range(5,0,-1):
            print(" "*(6-i)," *"*i)
    
    #PATTERN-ASCII VAlUE SIDE
    def pattern3(self):
        n=65
        for i in range(5,0,-1):
            for k in range(1,6-i):
                print(" ",end="")
            for j in range(1,i+1):
                print(chr(n),end="")
                n+=1
            print()



obj=A()
# print(obj.mid())pip install mysql-connector
obj.reverse()