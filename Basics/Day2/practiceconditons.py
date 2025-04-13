# number = int(input("Enter a number: "))
# if number % 2==0:
#     print("Even")
# else:
#     print("Odd")

n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
n3=int(input("Enter third number: "))
n4=int(input("Enter fourth number:"))
if n1>n2 and n1>n3 and n1>n4:
    print ("Largest number is: ",n1)
elif n2>n3 and n2>n4:
    print ("Largest number is: ",n2)
elif n3>n4:
    print ("Largest number is: ",n3)
else:
    print ("Largest number is: ",n4)
# if n1>n2 and n1>n3:
#     print ("Largest number is: ",n1)
# elif n2>n3:
#     print ("Largest number is: ",n2)
# else:
#     print ("Largest number is: ",n3)

# n4 = int(input("Enter a number: "))
# if n4 % 7==0:
#     print("Divisible by 7")
# else:
#     print("Not divisible by 7")