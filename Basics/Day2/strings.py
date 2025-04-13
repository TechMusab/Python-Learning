str1= "this is a string"
str2= ' this is also a string'
str3= """ this is a string"""
print(str1)
str4= str1 + str2
print(str4)
print(len(str1))
print(str1[0])
# str[3]='J' not allowed
print(str1[0:4])
print(str1[0:])
print(str1.endswith('string'))
print(str1.startswith('this'))
print(str1.find('is'))
print(str1.count('is'))
print(str1.upper())
print(str1.lower())
print(str1.title())
print(str1.split(' '))
print(str1.split('i'))
print(str1.replace('is','was'))
print(str1.strip())
print(str1.lstrip())
print(str1.rstrip())
