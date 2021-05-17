#Silicing of array
from  array import *
# sample of an array
a=array('i',[10,20,30,40,50,60,70,80])
print(a)
print(type(a))
print("0th to 4th")
print(a[0:5])
print("[:]")
print(a[:])
print("3rd to last")
print(a[3:])
print("0th to 6th step 2")
print(a[0:7:2])
print("[-4:] Last(-4-(-8))=4elements ")
print(a[-4:])
print("[-4::-1]=(-4 -4-1=-5 -5-1=-6 -6-1=-7)")
print(a[-4::-1])
print("[-4::1]=(-4 -4+1=-3 -3+1=-1 -2+1=-1)")
print(a[-4::1])
print("[-4::-2]=( -4 -4-2=-6 -6-2=-8)")
print(a[-4::-2])
print("a[-4:-1]")
print(a[-4:-1])
print("a[90:]")
print(a[90:])
print("-4::-7")
print(a[-4::-7])
print("a[-1::-1]")
t=a[-1::-1]
print(t)
print("a=",a)
print("after reverseing t")
t.reverse()
print(t)





# creating an empty array
