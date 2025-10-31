def mid(s):
    
    result=0
    if len(s)%2==0:
        print("Enter a odd String")
    
    else:
        mid=len(s)//2
        result=s[mid-1]+s[mid]+s[mid+1]
    
    return result
       
user=input("Enter name: ")
# result=mid(user)
# print(result)
print(mid(user))