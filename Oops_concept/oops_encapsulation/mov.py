movie={}
# gold=[]
# sliver=[]
# paltinum=[]


def Admin():
    menu="""
    Press 1 for Add movies
    Press 2 for Add seat Type To movies
    Press 3 for View movies
    """
    while True:
        print(menu)

        a_choice=int(input("Enter Choice:"))

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

            # seat_n=int(input("Enter seat number"))
            # for i in range(1,gold_n+1):
            #     gold.append(i)
            # for i in range(1,sliver_n+1):
            #     sliver.append(i)
            # for i in range(1,paltinum_n+1):
            #     paltinum.append(i)
            movie[movies_name]['seat']['gold']=[i for i in range(1,gold_n+1)]
            movie[movies_name]['seat']['sliver']=[i for i in range(1,sliver_n+1)]
            movie[movies_name]['seat']['paltinum']=[i for i in range(1,paltinum_n+1)]
            print(movie)

        elif a_choice==3:
            # print("Movie name is:",movies_name)
            # for i,j in movie[movies_name]['seat'].items():
            #         print("Movie Seat is",i)
            #         print("Available seat is :",j)
                    # print(f"Movie name is {movies_name}\nmovie seat is {i}\navailable seat is {j}")
            # movie_seat=movie[movies_name]['seat'][seat_type]
            # print("Movie name is:", movies_name)
            # print("Movie Seat is:", seat_type)
            # print("Available seats are:", movie_seat)
            # movie_seat_gold = movie[movies_name]['seat']['gold']
            # movie_seat_sliver = movie[movies_name]['seat']['sliver']
            # movie_seat_platinum = movie[movies_name]['seat']['paltinum']

            for key,value in movie.items():
                print("Movie name:",key)
                for seat_type,seats in value['seat'].items():
                    print("Seat type:",seat_type)
                    print("Seat",seats)
 

        elif a_choice==4:
            break


def Custmore():
    menu="""
    Press 1 for search movies
    Press 2 for  seat Type of movies
    Press 3 for View movies
    """
    while True:
        print(menu)
        c_choice=int(input("Enter Choice:"))

        if c_choice==1:
            movies_name=input("Enter Movie Name:").lower()

            if movies_name in movie:
                print(f"Movie {movies_name} is available")
                print("Avalable seat:",movie[movies_name]['seat'])
        



Admin()
Custmore()



