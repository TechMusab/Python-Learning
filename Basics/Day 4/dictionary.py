#key valur pair
# word-> meaning
info={
    "key":"value",
    "name":"musab",
    "learning":"Coding",
    "age":"18",
    "marks":[23,43,55],
    "topics":("dict","set")
}
#dictionaries are mutable
#don't allow duplicates
info["name"]="joiya"
info["surname"]="Ubaid"
# print(info)
#nested dictionaries
student={
    "name":"Musab",
    "subjects":{
        "phy":98,
        "chem":87,
        "math":87,
                }
    
    
}
print(student["subjects"]["math"])
print(list(student.keys()))
print(len(student))
print(len(list(student.keys())))
print(student.values())
print(student.items())
#print(student["name2"]) # error
print(student.get("name2")) # This gives none
student.update({"city":"islamabad"})
print(student)