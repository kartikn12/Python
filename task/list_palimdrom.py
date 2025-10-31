# l=[]
# n=int(input("Num:"))


# for i in range(1,n):
#     a=int(input("Num:"))
#     l.append(a)
# print(l)

# last=l[-1]
# slast=l[-2]


# for i in range(0,3):
#     if l[i]==last:
#         if l[1]==slast:
#             print("p")
#         else:
#             print("N")

# l1=l

# if l==l1:
#     print("P")
# else:
#     print("N")

l=[]
n=int(input("Num:"))

for i in range(n):
    a=int(input("Num:"))
    l.append(a)

print(l)

n3=len(l)//2
print(l[len(l)-1]-i)
ans="palimdrome"

for i in range(0,n3):
    if l[i]==l[len(l)-1-i]:
        continue
    else:
        ans="not"
        break
print(ans)
