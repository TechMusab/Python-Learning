# f=open('file.txt',"r")
# data= f.read(5)
# data2=f.readline()  
# # print(data)
# print(data2)
# print(type(data))
# f.close()
# f=open('file.txt','a')
# f.write("hello\n")
# f.close
# f=open("file.txt","r+")
# f.write("ajh")
# print(f.read())
# f=open("file.txt","w+")
# print(f.read())
# f=open("file.txt","a+")
# print(f.read())
# f.write("Hello")
# f.close()
# with open('file.txt','r') as f: # with auto closes the file
#     data=f.read()
#     print(data)
    
#for deleting the file
import os
os.remove("file.txt")