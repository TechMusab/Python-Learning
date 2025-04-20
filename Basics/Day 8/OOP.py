# to prevent redundency and increase reusability
class Student:
    def __init__(self,name):
        self.name=name
        print("Adding new student in Database...")
    

s1=Student("Musab")
print(s1.name)
# print(s1)


# class  Car:
#     color="blue"
    
# c=Car()
# print(c.color)    