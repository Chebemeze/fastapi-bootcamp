# def square(x):
#     return x * x

# print(square(5))
# print("After applying lambda:")

# numbers = [8,2,3,4,5]
# a = (x*x for x in numbers)
# print(list(a))
# print(next(a))

# # lambda
# a = filter(lambda x: x%2 == 0, numbers)
# b = sorted(numbers)
# print(b)

# cart = [{"item": "cup", "qty": 10}, {"item": "spoon", "qty": 3}]
# sorted_cart = sorted(cart, key=lambda x: x["qty"])
# print(sorted_cart)

#utilizing a class method to solve
# cls (the name of the class)
class Student:
    #general variable for all objects of this class
    school: "Abia State University"

    @classmethod
    def change_school(cls, new_name):
        cls.school = new_name

#creating a new Student Object.
gometo = Student()
gometo.change_school("Learn2Earn")
print(gometo.school)

class Courses:
    pass
class Level:
    pass
class Student(Courses, Level):
    pass
print(Student.__mro__)

class CardboardCup:
    def __init__(self, ounces):
        self.contents_ounces = float(ounces)
        
    # __len__ must return a standard integer
    def __len__(self):
        return int(self.contents_ounces)

my_cup = CardboardCup(8.5)
current_volume = len(my_cup)