m1=input("Enter 1st favourtie movie:")
m2=input("Enter 2nd favourtie movie:")
m3=input("Enter 3rd favourtie movie:")
l=[m1,m2,m3]
print(l)


#palindrome
p=[1,2,1]
p2=p.copy()
p2.reverse()
if p==p2:
    print("palindrome")
else:
    print("not palindrome")



grades=["C","D","A","A","B","B","A"]
print(grades.count("A"))


grades.sort()
print(grades)
