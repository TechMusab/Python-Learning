def sumnatural(n):
    if n==0:
        return 0
    return sumnatural(n-1)+n

print(sumnatural(4))

def printelements(list,index):
    if index==len(list):
        return
    print(list[index])
    return printelements(list,index+1)
cities=["isb",'lhr',"rwp"]
printelements(cities,0)