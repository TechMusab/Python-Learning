class Student:
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    
    
    def average(self):
        return (self.m1+self.m2+self.m3)/3


s1=Student(34,56,78)
s2=Student(45,67,89)
print(s1.average())
print(s2.average())
