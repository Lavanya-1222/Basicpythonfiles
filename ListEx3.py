# ------------------Slicing on list---------------------
a=[1,2,3,4,5,6,7]
print(a)
b=a[1:5]
print("a[1:5] =",b)
b=a[0:]
print("a[0:] =",b)
b=a[0:3]
print("a[0:3] =",b)
b=a[-4:]
print("a[-4:] =",b)
b=a[0:7:2]
print("a[0:7:2] =",b)
b=a[-5:-3]
print("a[0:] =",b)
b=a[-4:]
print("a[-4:] =",b)
b=a[-4::1]
print("a[-4::-1] =",b)
b=a[-4::-1]
print("a[-4::-1] =",b)
b=a[-4::2]#-4+(2)=-2
print("a[-4::2] =",b)
b=a[-4::-2]#-4+(-2)=-6
print("a[-4::-2] =",b)
b=a[-4::-7]#-4+(-7)=-11
print("a[-4::-7] =",b)
b=a[-4::7]#-4+(7)=3
print("a[-4::-7] =",b)
b=a[-1::-1]#-1+(-1)=-2->+(-1)=-3->-3+(-1)
print("a[-1::-1] =",b)
b.reverse()
print(b)