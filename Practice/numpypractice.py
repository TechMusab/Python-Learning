import numpy as np 
arr=np.random.randint(1,100,size=(5,5))
#np.where(condition,true,false)
matrixafter=np.where(arr%2 !=0,-1,arr)
print(arr)
print("\nMatrix after replacing odd numbers with -1:")
print(matrixafter)
maxrow=np.max(arr,axis=1)
print("\nMax of each row:")
print(maxrow)
# Create 100 evenly spaced numbers from 0 to 10
evenly_spaced = np.linspace(0, 10, 100)
print("\nArray of 100 evenly spaced numbers between 0 and 10:")
print(evenly_spaced)
