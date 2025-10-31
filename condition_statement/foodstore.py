print("Press 1 for Dabeli....30")
print("Press 2 for vadapav.....25")
print("Press 3 for sandwhich.....60")
print("Press 4 for puff....30")

n = int(input("Enter number: "))
prize=0 

if n==1:
    print("You choose dabeli...30/-")
    prize=30
    
   

elif n==2:    
    print("You choose vadapav...25/-")
    prize=325
    
   

elif n==3:    
    print("You choose sandwhich...60/-")
    prize=60
    
   
elif n==4:    
    print("You choose puff...30/-")
    prize=30

    
else:
    print("invalid")
 
quntity = int(input("enter quntity: "))    #quntity from user    
bill = prize*quntity #genrate normal bill
gstbill=prize*quntity*8/100 #gst bill genrate
print("Your bill is",bill+gstbill) #total bill