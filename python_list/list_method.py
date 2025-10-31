'''
collections
List-tuple-dictionary-set

List-list is a collection data type in python we can store multiple values in single variable 
list is mutable,ordered and allow duplicate value
denote with []
'''

l=[1,1,True,"java","python",2.45,31]

print(type(l)) #defind type

l.append(3.45) #append at last value
print(l)

print(l.count(1))# how many time value repetad in list show number


l.extend([2,5,8])
print(l)

print(l.index("java"))#give value it will show in which index it has

l.insert(3,"c++") #insert value in particular index
print(l)

l.pop(2) # if we give index value in breaket it will remove through that value in that index
print(l) # remove value at last 

l.remove("java") #remove particular value that we give
print(l)


