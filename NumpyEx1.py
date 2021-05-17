# 1D array in Numpy
from numpy import *
print("sample of an array")
a=array([10,20,30,40,50,60,70,80])
print(a)
print(type(a))
print("Accessing 1D array")
print(print(a[0]))
print("Accsssing with for loop")
print("Without index ")
for i in a:
    print(i,end=" ")
print("\nWith index")
for i in range(len(a)):
    print(a[i],end=" ")
print("\nwhile loop:")
i=0
while i<len(a):
    print(a[i],end=" ")
    i+=1
print("\n*******linespace(strat,end,num,dtype)********")
b=linspace(1,8,5)
print(b)
print("\n*******logspace(strat,end,num,dtype)********")
c=logspace(1,3,5)
print(c)
print("\n*******arange(strat,end,step,dtype)********")
d=arange(1,8,1)
print(d)
print("\n*******zeros(shapes,dtype)********")
e=zeros(5,)
print(e)
print("\n*******ones(shapes,dtype)********")
f=ones(5,)
print(f)
print("\n*******reshape(arra_name,(no.of.arrays,rows,columns)********")
r=array([10,2,3,4,5,6])
print(r)
r1=reshape(r,(1,2,3))
print(r1)
print("\n**************MATH OPERATOR************")
print(a)
c=a+2
d=a*2
print(d)
print(c)
d=[10,200,300,40,5000, 60,700,80]
print("a",a)
print("d",d)
r=a==d
print(r)
r=a<d
print(r)
print("\n*******all()********")
print(any(a<d))
print(all(a<d))
print("\n*******where()********")
print(a)
print(d)
w=where(a==d,a,d)
print(w)
print("\n*******nonzero()********")
nz=array([10,2,0,5,0,89])
s=nonzero(nz)
print(s)
print("\n*******copy()********")
cp=nz.copy()
print(cp)
cp[0]=909
print(cp)
print(nz)
print("\n*******view()********")
v=nz.view()
print(v,id(v))
print(nz,id(nz))
v[0]=76
print(v,id(v))
print(nz,id(nz))
print("\n*******Alising********")
print()
A=array([10,20,309,434])
B=A
print(A,id(A))
print(B,id(B))
B[0]=76
print()
print(A,id(A))
print(B,id(B))
print()
A[1]=658
print()
print(A,id(A))
print(B,id(B))
print("==============all===========")
p=[10,20,30]
q=[10,20,30]
print(all(p<q))

print("\n*******UserInput Array********")
n=int(input("Enter No.of Elements"))
us=zeros(n,dtype=int)
print(us)
for i in range(n):
    us[i]=int(input("Enter Number:"))
for i in us:
    print(i,end=" ")

