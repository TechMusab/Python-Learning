# to prevent redundency and increase reusability
# class Student:
#     uni_name="ABC University"
#     #default constructor
#     def __init__(self):
#         pass
#     #parametrized constructor
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
    
#     def hello(self):
#         print("Welcome")
#     def getmarks(self):
#         print("Marks:",self.marks)

# s1=Student("Musab",98)
# print(s1.name)
# print(s1.marks)
# print(s1.uni_name)
# s1.hello()
# s1.getmarks()
# class attributes ==> are common in class
# object attributes==> specific to objects
# obj attr > class atr (precedence)


# Static method
# allow to wrap function in class to change its behavior
# class Student:
#     uni_name="ABC University"
#     #default constructor
#     def __init__(self):
#         pass
#     #parametrized constructor
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
    
#     @staticmethod
#     def hello():
#         print("Welcome")

# s1=Student("Musab",98)
# s1.hello()
    
# Pillars of OOP
# 1.Abstraction
#   ==> Hiding the implementation details and showing only functionality to the user.
#   ==> It helps to reduce programming complexity and increase efficiency.
# 2.Encapsulation
#   ==> Wrapping the data and the methods into a single unit.
# 3.Inheritance
# 4.Polymorphism

class Account:
    def __init__(self, no, balance):
        self.no = no
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)
        
    def withdraw(self, amount):
        self.balance-=amount
        print("Withdrawn:", amount)
    
    def get_balance(self):
        print("Balance:", self.balance)

a1= Account(101, 1000)
a1.deposit(500)
a1.withdraw(200)
a1.get_balance()