import  random
otp=random.randint(1001,9999)
d={}

while True:
    
    menu='''
    press 1 for signup
    press 2 for login
    press 3 for forgetpassword
    press 4 for exit

    '''
    print(menu)
    
    ch=int(input("enter choice "))
    try:
        
        if ch==1:
            
            name=input("enter name ")
            email=input("enter email ")
            mno=int(input("Enter mobile number "))
            password=int(input("Enter password "))
            cpassword=int(input("Enter confirm password "))
            
            if password==cpassword:
                    d['email']=email
                    d['mno']=mno
                    d['password']=password
                    
                    print("Your signup succesful!!")
            else:
                print("Enter correct password")
        elif ch==2:
            email=input("enter email ")
            password=int(input("Enter password "))
            
            if d['email']==email and d['password']==password:
                print("Your login successful!")
            else:
                print("enter a wrong email or password")
        elif ch==3:
            mno=int(input("Enter mobile number "))
            
            if d["mno"]==mno:
                print("Your otp is ",otp)
                
                uotp=int(input("Enter a otp "))
                
                if otp==uotp:
                    password=int(input("Enter a new password "))
                    d["password"]=password
                else:
                    print("Enter a vaild number")
        elif ch== 4:
            print("thankyou")
            break
        else:
            print("enter valid choice")
            break
    except Exception as e:
        print(e)
        print("Invalid input")
        
        
                
        