def fun1(n):

    rem=0
    result=0
    n1=n
    while (n!=0):
        rem=n%10
        result**=rem
        print(result)
        n=n//10

    if (n1==result):
            print("Armstrong")
    else:
            print("not")
            

fun1(153)


# def power_n(num,power):
    
#     if num==0:
#         return 0

#     else: 
#        return (num%10)**power + power_n(num//10,power)

# def arm(num):
#     dig=len(str(num))

#     return num==power_n(num,dig)
    

# num=int(input())
# if arm(num):
#     print("yes")
# else:
#     print("no")





