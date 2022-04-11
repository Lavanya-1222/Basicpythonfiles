# Numpy Slicing 2d array
from numpy import *
print("sample of 2d array")
a=array([[10,20,30],
         [40,50,60]])
print(a)
print("------a[:,:]------")
print(a[:,:])
print("------a[1:,2:]------")
print(a[1:,2:])
print("------a[0:,1:]------")
print(a[0:,1:])
print("------a[0:,0:2]------")
print(a[0:,0:2])
print("------a[0:2,1:3]------")
print(a[0:2,1:3])
print("------a[1,1:]------")
print(a[1,1:])
print("------a[0,0]------")
print(a[0,0])
print("------a[:,1]------")
print(a[:,1])