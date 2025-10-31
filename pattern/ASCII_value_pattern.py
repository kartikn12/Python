n=65
for i in range(1,6):
    for j in range(1,i+1):
        print(chr(n),end="")
        n+=1
    print()

for i in range(1,6):
    print(chr(n)*i)
    # n+=1