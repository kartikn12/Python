even = 0
evensum = 0
odd = 0
oddsum = 0

for i in range(1, 6):
    n = int(input("Enter number:: "))
    if n % 2 == 0:
        print("Number is even")
        even += 1
        evensum += n
    else:
        print("Number is odd")
        odd += 1
        oddsum += n

print("Total even numbers:", even)
print("Total sum of even numbers:", evensum)
print("Total odd numbers:", odd)
print("Total sum of odd numbers:", oddsum)
