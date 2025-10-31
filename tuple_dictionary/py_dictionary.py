d={1:"h1",2:"h2","h3":3,4:"h4"}

print(d)
print(type(d))

d.update({5:"h5",6:"h6"}) #add in last
print(d)

d.pop('h3') #pop a value there as key h3 remove it's key and value
print(d)

d.popitem()#remove last item
print(d.items()) # show every item
print(d.keys())#show only keys
print(d.values())#show only values
print(d.get(1)) # give key it will give it's value


t=(1,2,3,4)
d1={}

print(d1.fromkeys(t)) # in every tuple value it assign as key in dictionary value will be none(null)
print(d1.fromkeys(t,20))#if we want give value we can only give one value to every key

