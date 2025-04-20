# to prevent redundency and increase reusability
class Student:
    uni_name="ABC University"
    #default constructor
    def __init__(self):
        pass
    #parametrized constructor
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    
    def hello(self):
        print("Welcome")
    def getmarks(self):
        print("Marks:",self.marks)

s1=Student("Musab",98)
# print(s1.name)
# print(s1.marks)
# print(s1.uni_name)
s1.hello()
s1.getmarks()
# class attributes ==> are common in class
# object attributes==> specific to objects
# obj attr > class atr (precedence)