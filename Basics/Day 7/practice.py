# f=open('practice.txt','a')
# f.write('Hi everyone\n we are learning File I/O\nusing Java\n i like programmin in Java.')
# f.close()

# with open('practice.txt','r') as f:
#     data=f.read()
    
# newdata=data.replace("Java","Python")
# print(newdata)

# with open('practice.txt','w') as f:
#     f.write(newdata)
    
    
with open('practice.txt','r') as f:
    data=f.read()
    if(data.find('learning')!=-1):
        print('found')
    else:
        print('notfound')