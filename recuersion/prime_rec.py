def pr(n,i=2):

    if n<1:
        return False
    if i*i>n:
        return True
        
    if n%i==0:
        return False
    return pr(i+1)  

            
print(pr(91))