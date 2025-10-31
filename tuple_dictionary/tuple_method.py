'''
tuple-is a collection data type we can store multiple value 
denote with- ()
immutable-not changeble
faster than list

dictionary-collection store key and value pair - denote with-{} - changeble(mutable)
'''

t=(1,2,"py",3.12,2.23)

print(type(t))

print(t.index('py')) # give value in it will give index number where is that value are stored

print(t.count(2)) # how many time value are used in tuple give its count


#for changes in tuple we convert into list than we can change in tuple

l=list(t)
print(l)

l.extend([1,20,3])

t1=tuple(l)

print(t1)