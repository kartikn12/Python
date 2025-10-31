l=[2,0,4,0,6,0,8,0,1]

temp=0
l1=0
# l2=[]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l1==l[i]:
            temp=l[i]
            l[i]=l[j]
            l[j]=temp
        

print(l)


n=len(l)
i=0
j=n-1

