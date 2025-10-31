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
        break
    elif user in choice or choice in user:
        print("You are too close")
    else:
        print("Better luck next time")
else:
    print("The correct word was:", choice)
