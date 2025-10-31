from abc import ABC

class Emoloyer(ABC):

    def salary(self):
        pass

class Xyz(Emoloyer):
    def salary(self):
        print("Salary 30k")

class Yyz(Emoloyer):
    def salary(self):
        print("Salary 12k")

obj=Yyz()
obj.salary()

obj1=Xyz()
obj1.salary()