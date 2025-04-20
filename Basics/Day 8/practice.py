# class Student:
#     def __init__(self,m1,m2,m3):
#         self.m1=m1
#         self.m2=m2
#         self.m3=m3
    
    
#     def average(self):
#         return (self.m1+self.m2+self.m3)/3


# s1=Student(34,56,78)
# s2=Student(45,67,89)
# print(s1.average())
# print(s2.average())

# problem 2

# class Circle:
#     def __init__(self,r):
#         self.r=r
#     def area(self):
#         return 3.14*self.r*self.r
#     def parameter(self):
#         return 2*3.14*self.r
#     def display(self):
#         print("Area of circle is",self.area())
#         print("Parameter of circle is",self.parameter())

# c1=Circle(5)
# c1.display()


# Problem 3
# class Employee:
#     def  __init__(self,role,department,salary):       
#         self.role=role
#         self.department=department
#         self.salary=salary
#     def showdetails(self):
#         print(self.role,self.department,self.salary)

# e=Employee("engineer","development",70000)
# e.showdetails()

# class Engineer(Employee):
    
#     def __init__(self,name,age,role,department,salary):
#         super().__init__(role,department,salary)
#         self.name=name
#         self.age=age

# Problem 4
class Order:
    
    def __init__(self,item,price):
        self.item=item
        self.price=price
        
    #Dunder ftn
    def __gt__(self,o2):
        if(self.price>o2.price):
            print("o1 is greater then o2")
        else:
            print("o1 is not greater then o2")

o1=Order("chair",1000)
o2=Order("Table",900)
print(o1>o2)