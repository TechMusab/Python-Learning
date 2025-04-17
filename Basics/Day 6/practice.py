cities=["isb","lhr","rwp"]
def calulate_length(cities):
    return len(cities)
def printelements(cities):
    for city in cities:
        print(city,end=" ")
print(calulate_length(cities))
print(printelements(cities))

def factorial(n):
    fact=1
    for i in range(2,n+1):
        fact=fact*i
    return fact
print(factorial(7))

