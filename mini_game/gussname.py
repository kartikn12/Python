import random

computer=['python','java','php']

choice = random.choice(computer)

print("------Gusess the word------")

computer_word= choice[0]+"_"*(len(choice)-2)+choice[-1]


print("Word:",computer_word)

for i in range(1,4):
    
    print(f"-------round {i}-------")
    
    user=input("Gusess Your word:")
    user=user.lower()
    
    if choice==user:
        print("Your answer is correct")
    elif choice<user:
        print("You are too close")
    # elif choice>user:
    #     print("You are too far")
    
    else:
        print("Better luck next time")
        break
        
        
    
    