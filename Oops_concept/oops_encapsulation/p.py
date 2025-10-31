movie={}
price={'gold':200,'sliver':350,'paltinum':550}
def Admin():
    menu="""
    Press 1 for Add movies
    Press 2 for Add seat Type To movies
    Press 3 for View movies
    Press 4 for main menu
    
    """
    while True:

        print(menu)

        a_choice=int(input("Enter Choice:"))
        try:
            if a_choice==1:
                movies_name=input("Enter Movie Name:").lower()

                if movies_name in movie:
                    print("Already Exist")
                else:
                    movie[movies_name]={'seat':{}}
                    print(f"Movie {movies_name} Added")

            elif a_choice==2:
                
                movies_name = input("Enter Movie Name to add seats: ").lower()

                if movies_name not in movie:
                    print(f"There is no movie name:{movies_name}")
                    continue
                gold_n=int(input("Enter gold seat"))
                sliver_n=int(input("Enter sliver seat"))
                paltinum_n=int(input("Enter palitinum seat:"))


                movie[movies_name]['seat']['gold']=[i for i in range(1,gold_n+1)]
                movie[movies_name]['seat']['sliver']=[i for i in range(1,sliver_n+1)]
                movie[movies_name]['seat']['paltinum']=[i for i in range(1,paltinum_n+1)]
                print(movie)

            elif a_choice==3:


                for key,value in movie.items():
                    print("Movie name:",key)
                    for seat_type,seats in value['seat'].items():
                        seat_price=price.get(seat_type)
                        print("Seat type:",seat_type,"Price:",seat_price)
                        print("Seat",seats)

    

            elif a_choice==4:
                break
        except Exception as e:
            print(e)
        

def User():
    menu="""
    Press 1 for search movies
    Press 2 for  Book Ticket
    Press 3 for View movies
    Press 4 for main menu
    """
    while True:
        print(menu)
        c_choice=int(input("Enter Choice:"))
        try:
            if c_choice==1:
                movies_name=input("Enter Movie Name:").lower()
                if movies_name in movie:

                    for key,value in movie.items():
                        print("Movie name:",key)

                        for seat_type,seats in value['seat'].items():
                            seat_price=price.get(seat_type)
                            print("Seat type:",seat_type,"Price:",seat_price)
                            print("Seat",seats)
                else:
                    print(f"No movie available of {movies_name}")

            if c_choice==2:

                for key,value in movie.items():
                    print("Movie name:",key)
                    for seat_type,seats in value['seat'].items():
                        seat_price=price.get(seat_type)
                        print("Seat type:",seat_type,"Price:",seat_price)
                        print("Seat",seats)

                movies_name=input("Enter Movie Name:").lower()

                if movies_name in movie:
                    ticket=input("Enter your seat type for booking(gold/sliver/paltinum)").lower()
                    ticket_num=int(input("how many you want:"))
                    book_price=price.get(ticket)
                    seat_price=book_price * ticket_num    
                    gst=seat_price*0.18
                    final_price=seat_price+gst
                    
                    if ticket in movie[movies_name]['seat']:
                        available_seat = movie[movies_name]['seat'][ticket]
                        
                        for i in range(1,ticket_num+1):
                            seat_num=int(input(f"Enter seat number {i}:"))
                            if seat_num in available_seat:
                                available_seat.remove(seat_num)
                                print(f"{i} BOOKING DONE")
                            else:
                                print("Ticket not available!")
                    else:
                        print("Not found that type of ticket")
                else:
                    print(f"There is no movie name is {movies_name}")  
                print(f"{ticket_num} Ticket booked in {ticket} for {movies_name} movie")
                print(f"Your bill is: {final_price}")


            elif c_choice==3:
                for key,value in movie.items():
                    print("Movie name:",key)
                    for seat_type,seats in value['seat'].items():
                        seat_price=price.get(seat_type)
                        print("Seat type:",seat_type,"Price:",seat_price)
                        print("Seat",seats)

            elif c_choice==4:
                break
        except Exception as e:
            print(e)


while True:
    choice=int(input("Press 1 For Admin Side\nPress 2 for User Side\nPress 3 For Exit\nEnter choice:"))

    if choice==1:
        print("-------WELCOME TO ADMIN PANEL------")
        Admin()
    elif choice==2:
        print("-------WELCOME TO USER PANEL------")
        User()
    elif choice==3:
        print("--------THANK YOU------")
    else:
        print("Invalid Argument")





