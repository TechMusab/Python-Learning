#built in data type stores set of values
marks= [12,34,53,54,23]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(len(marks))
student=['musab',76,19]
print(student)
# lists are mutable while strings are mutable
student[0]='joiya'
print(student)
# print(student[3]) out of range
# for slicing there are same rules as string
print(marks[2:4])
print(marks[2:])
print(marks[-4:-1])


# List methods
student.append(4)
# student.sort()  not suportd for int and str
# student.sort(reverse=True) not supported
student.reverse()
student.insert(2,15) #(index,element)
student.remove(4) # removes th first occurence of element
student.pop(3) # reoves at particular index
print(student)