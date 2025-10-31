
i=1
even=0
evensum=0
odd=0
oddsum=0
while(i<=5):
   n = int(input("Enter number:: "))
   if n%2==0:
       print("number is even")
       even+=1
       evensum+=n
   else:
       print("number is odd")
       odd+=1
       oddsum+=n
   i+=1
print("Total even number:",even)
print("Total sum of even number",evensum)
print("Total odd number:",odd)
print("Total sum of odd number",oddsum)