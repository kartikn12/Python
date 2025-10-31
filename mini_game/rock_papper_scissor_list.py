import random

computer=['rock','paper','scissor']


menu="""
    Rock
    Paper
    Scissor
    """
    
print(menu)
uwin=0
cwin=0
draw=0
for i in range(1,6):
    print(f"--------------round {i}--------------")
    user=input("Enter choice:")
    user=user.lower()    
    
    if user == "1":
        user = "rock"
    elif user == "2":
        user = "paper"
    elif user == "3":
        user = "scissor"

    m1 = random.choice(computer)
    print("Your choice:", user)
    print("Computer choice:", m1)
      
    if user not in computer:
        print("invalid input")
        break 
      
    if user==m1:
        draw+=1
        print("Draw!!")
        
    elif user =="rock":
        
        if m1 =="Paper":
            cwin+=1
            print("Computer win")
        else:
            uwin+=1
            print("user win")
            
    
    
    elif user=='paper':
        
        if m1=='rock':
            uwin+=1
            print("user win")
        else:
            cwin+=1
            print("computer win")
            
    
    
    elif user=='scissor':
        if m1=='Paper':
            uwin+=1
            print("user win")
        else :
            cwin+=1
            print("computer win")

print("********Point Table*********")
print("User win:",uwin)
print("Computer Win:",cwin)
print("Draw:",draw)

if uwin==cwin==draw or uwin==cwin:
    print("******Game Draw******")
elif uwin>cwin:
    print("******User Win Game******")
else:
    print("******Computer Win Game******")
    

   
        
