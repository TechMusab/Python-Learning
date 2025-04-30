import numpy as np 

#Create a 5×5 matrix with random integers.
arr=np.random.randint(1,100,size=(5,5))
#Replace all odd numbers with -1.
matrixafter=np.where(arr%2 !=0,-1,arr)
print(arr)
print("\nMatrix after replacing odd numbers with -1:")
print(matrixafter)
#Find the row-wise maximum and minimum.
maxrow=np.max(arr,axis=1)
minrow=np.min(arr,axis=1)
print("\nMax of each row:")
print(maxrow)
print('\nMin of each row:')
print(minrow)
#Create an array of 100 evenly spaced numbers between 0 and 10.
evenly_spaced = np.linspace(0, 10, 100)
print("\nArray of 100 evenly spaced numbers between 0 and 10:")
print(evenly_spaced)
#Generate a 3x3 identity matrix.
identity=np.ones((3,3))
print(identity)