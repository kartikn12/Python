# l = [("a", 1), ("b", 2), ("c", 3),("d",40),
#         ("e",5),("f",6)]
# d = {}

# for i in range(len(l)):
#     d[l[i][0]] = l[i][1]
# print(d)


# d={"a":23,"c":34,"d":12}
d={}
m=[]
for i in range(2):
    a=input("name:")
    b=int(input("Marks:"))

    d[f"name-{i}"]=a
    d[f"marks-{i}"]=b
    m.append(b)
print(d)


max=m[0]

for i in m:
    if i>max:
        max=i
print(max)




   
    