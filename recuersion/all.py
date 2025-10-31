# #prime

# def fun(n,i=2):

#     if n<1:
#         return False
#     if i*i>n:
#         return True
#     if n%i==0:
#         return False
#     return fun(i+1)

# print(fun(4))

def fun1(n,power):
    if n==0:
        return 0
    
    else:
        return(n%10)**power+fun1(n//10,power)
    
def fun2(n):
    dig=len(str(n))
    return n==fun1(n,dig)

n=153
if fun2(n):
    print("hello")
else:
    print("op")