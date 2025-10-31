import random
# computer=['Rock','papper','scissor']
computer=random.randint(1,3)


# print(computer)
# print("Computer choice:",random.choice(computer))

menu="""
    Press 1 for Rock
    press 2 for Papper
    press 3 for scissor
    """

print(menu)


while True:
    user=int(input("Enter Your choice:"))
    print("Your Choice",user)
    print("Computer choice",computer)
    
    if user>3:
        print("Invalid")
        break
    elif user==computer:
        print("Tie")
        
        
    elif user==1:
        if computer==2:
            print("Computer win")
        elif computer==3:
            print("user win")
            
            
    elif user==2:
        if computer==1:
            print("user win")
        elif computer==3:
            print("computer win")
            
            
    else:
        if computer==2:
            print("user win")
        elif computer==1:
            print("computer win")

    
