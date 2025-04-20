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

# class Account:
#     def __init__(self, no, balance):
#         self.no = no
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         print("Deposited:", amount)
        
#     def withdraw(self, amount):
#         self.balance-=amount
#         print("Withdrawn:", amount)
    
#     def get_balance(self):
#         print("Balance:", self.balance)

# a1= Account(101, 1000)
# a1.deposit(500)
# a1.withdraw(200)
# a1.get_balance()

# del keyword
# del a1
# print(a1)

# class Account:
#     def __init__(self, no, balance,accpass):
#         self.no = no
#         self.balance = balance
#         self.__accpass=accpass
     
#     def resetpass(self, newpass):
#         self.__accpass=newpass
#         print("Password changed successfully")


# a1= Account(101, 1000, "abc123")
# a1.resetpass("xyz456")
# #print(a1.__accpass) # this will give error

# # inheritance

# class Parent:
#     def __init__(self):
#         print("Parent constructor")
    
#     def show(self):
#         print("Parent class method")

# class Child(Parent):
#     def __init__(self):
#         super().__init__() 
#         print("Child constructor")
    
#     def show(self):
#         super().show() 
#         print("Child class method")

# c1=Child()
# c1.show()

# single inhertance
# class Parent:
#     def __init__(self):
#         print("Parent constructor")
    
#     def show(self):
#         print("Parent class method")
# class Child(Parent):
#     def __init__(self):
#         super().__init__() 
#         print("Child constructor")
    
#     def show(self):
#         super().show() 
#         print("Child class method")
# c1=Child()
# c1.show()

# Multi level inheritance
# class Parent:
#     def __init__(self):
#         print("Parent constructor")
    
#     def show(self):
#         print("Parent class method")
# class Child(Parent): 
#     def __init__(self):
#         super().__init__() 
#         print("Child constructor")
    
#     def show(self):
#         super().show() 
#         print("Child class method")
# class GrandChild(Child):
#     def __init__(self):
#         super().__init__() 
#         print("GrandChild constructor")
    
#     def show(self):
#         super().show() 
#         print("GrandChild class method")
# g1=GrandChild()
# g1.show()

# Muliple inheritance
class Parent1:
    def __init__(self):
        print("Parent1 constructor")
    
    def show(self):
        print("Parent1 class method")
class Parent2:
    def __init__(self):
        print("Parent2 constructor")
    
    def show(self):
        print("Parent2 class method")
class Child(Parent1, Parent2):
    def __init__(self):
        super().__init__() 
        print("Child constructor")
    
    def show(self):
        super().show() 
        print("Child class method")
c1=Child()
c1.show()

# class method
class Person:
    name="anonymous"

    # def change_name(self, new_name):
    #     self.__class__.name=new_name
    @classmethod
    def change_name(cls, new_name):
        cls.name=new_name

p1=Person()
p1.change_name("Musab")
print(Person.name)
# 3 types of methods
# 1. instance method
# 2. class method
# 3. static method

# @ property decorator
class Student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
    
    @property
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3) + "%"

s1=Student(90,80,70)
print(s1.percentage)
s1.phy=66
print(s1.percentage)

# Polymorphism