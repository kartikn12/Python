l=[12,34,56,78,45,23]    
i=0
j= -1

while l[i]>l[j]:
    l[i],l[j]=l[j],l[i] 
    i+=1
    j-=1 
      
print(l)

