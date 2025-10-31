# #1] Positional Arguments (based on order)
def student (name,age):
    print(name,age)

student("nikhil",22)

# 2] Keyword Arguments

def student1(name,age):
    print("name:",name)
    print("age:",age)

student1(age=22,name="nikhil")

#3]Default Argument

def student2(name,city="goa"):
    print("name:",name)
    print("city",city)
    
student2("nikhil")
student2("anuj","mumbai")

#4.A] Variable-Length Arguments
#*args → for multiple positional arguments

def total_marks(*marks):
    # print(type(marks))
    print("marks:",marks)
    print("total:",sum(marks))
    
total_marks(22,33,44,33,32)

#4.B]**kwargs → for multiple keyword arguments

def student_into(**into):
    for key,value in into.items():
        print(key,":",value)
        
student_into(name="nikhil",course="B.tech",age=23)
