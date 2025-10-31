"""
lamda function
annoyms of function
multiple number of argument
expression singl

syntax: lamda a: return a*a*a
"""

# n=lambda a,b,c,d:a+b*(c+d)

# print(n(1,2,3,4))

# n=lambda x:"positive" if x>0 else "negative" if x<0 else "zero"

# print(n(1))
# print(n(-1))
# print(n(0))


# n= lambda x:"even" if x%2==0 else "odd"
# print(n(19))
# print(n(24))

# n=lambda a,b,c,d:[a,b,c,d]

# print(n(2,3,4,5))

# for i in n:
#     print(i)

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


n= [lambda arg=x:arg*10 for x in range(1,5)]

for i in l:
    print(i())

# l=[12,34,56,78,45,23]    
# i=0
# j= -1

# while l[i]>l[j]:
#     l[i],l[j]=l[j],l[i] 
#     i+=1
#     j-=1 
      
# print(l)       
