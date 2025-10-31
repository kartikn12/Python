print("1st program:")

def fun(l:list):
    
    
    print("small:",l[0])
    print("large set:",l[-1])
    print("large set 2:",l[-2])

user=[23,45,67,89,87]
user.sort()
fun(user)
print("2nd program:")

def fun0(m , n):
    
    l=[]
    ev=[]
    od=[]
    for i in range(m,n):
    
        l.append(i)
        
        if i%2==0:
            ev.append(i)
        else:
            
            od.append(i)
    print(l)
    print(od)
    print(ev)

fun0(1,21)
print("3rd program:")
def fun1(*m):
    l1=[]
    l2=[]
    for i in m:
        if i not in l1:
            l1.append(i)    
        else:
            l2.append(i)

    print(l1)
    print(l2)    

fun1(1,2,3,1,2)