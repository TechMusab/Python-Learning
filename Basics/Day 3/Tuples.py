# tuples are brothers of list
# tuples are immutable the big difference with lists
tup=(34,22,43,43,23)
# tup[0]=2 error
tup1=()
print(tup)
print(tup1)
tup2=(1,) #must seprate with comma if not python treates it as a integer
print(tup2)
print(type(tup2))
# Slicing works as similar as strings
print(tup.index(43))
print(tup.count(43))