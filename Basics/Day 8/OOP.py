# to prevent redundency and increase reusability
class Student:
    #default constructor
    def __init__(self):
        pass
    #parametrized constructor
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        print("Adding new student in Database...")
    

s1=Student("Musab",98)
print(s1.name)
print(s1.marks)
# print(s1)


# class  Car:
#     color="blue"
    
# c=Car()
# print(c.color)    