d1={'p':600,'q':300,'r':400}
d2={'p':300,'q':200}
ans={}
# ans={'p':d1['p']+d2['p'],'q':d1['q']+d2['q']}

for i,j in d1.items():
    for k,l in d2.items():
        
        if i==k:
            ans[i]=j+l
print(ans)

l=[3,4,5]
l1=[12,45,63]
d3={} # if only value given it will store AS SET

for i in range(len(l)):    
   d3[l[i]]=l1[i]
print(d3)

