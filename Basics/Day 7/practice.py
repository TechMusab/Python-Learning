# f=open('practice.txt','a')
# f.write('Hi everyone\n we are learning File I/O\nusing Java\n i like programmin in Java.')
# f.close()

# with open('practice.txt','r') as f:
#     data=f.read()
    
# newdata=data.replace("Java","Python")
# print(newdata)

# with open('practice.txt','w') as f:
#     f.write(newdata)
    
    
# with open('practice.txt','r') as f:
#     data=f.read()
#     if(data.find('learning')!=-1):
#         print('found')
#     else:
#         print('notfound')


def checkforword(word):
    data=True
    lineno=1
    with open('practice.txt','r') as f:
        while data:
            data=f.readline()
            if(word in data):
                print(lineno)
                return
            lineno+=1
    return -1

checkforword("Python")
def counteven():
    sum=0
    with open('practice.txt','r') as f:
        data=f.read()
        l=data.split(',')
        print(l)
        for n in l:
            n=int(n)
            if(n%2==0):
                sum+=n
    return sum
print(counteven())