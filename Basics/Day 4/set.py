# Set is a collection of unordered items 
# and each collection is immutable
collection={1,2,2,2,3,4}
print(collection)
print(type(collection))
print(len(collection))
c1={} #dictonary
c2=set() #set
#set is mutable
# elemeents are mutable
s1=set()

s1.add(1)
s1.add(2)
s1.remove(1)
# s1.remove(3)
print(s1)
# s1.add([1,2,2]) error unhasble type
s1.add((1,2,3))
s1.clear()
#s1.pop() removes a random value
a1={1,2,3}
a2={2,1,4}
print(a1.union(a2))
print(a1.intersection(a2))