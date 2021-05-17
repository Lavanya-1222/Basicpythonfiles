# ------------------Nested tuple-----------------
print("------------Nested tuple-1------------")
a=(10,20,30,(50,60))
print(a)
print("------------accessing Nested tuple-1------------")
a=(10,20,30,(50,60))
print(a[3][0])
print("-------------------accessing Nested tuple-1-for loop---------------")
a=(10,20,30,(50,60))
for i in range(len(a)):
    if type(a[i]) is tuple:
       for j in range(len(a[i])):
           print(a[i][j],end=" ")
    else:
        print(a[i],end=" ")
print("\nwhile loop")
i=0
while i<len(a):
    if type(a[i]) is tuple:
        j=0
        while j<len(a[i]):
            print(a[i][j],end=" ")
            j+=1
    else:
        print(a[i],end=" ")
    i+=1
print("------------Nested tuple-2------------")
a=((10,20,30),(40,50,60))
print(a)
print("------------accessing Nested tuple-1------------")
print(a[1][2])
print("-------------------accessing Nested tuple-1-for loop---------------")
print("without index")
for i in a:
    for j in i:
        print(j,end=" ")
print("\nwith index")
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j],end=" ")
print()
print("while loop")
i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        print(a[i][j],end=" ")
        j+=1
    i+=1
print()
print("----------------------------------Slicing Nested List----------------------------------")
a=((10,20,30),(40,50,60),(70,80,90),(11,22,33))
print("a[0:]",a[0:])
print("a[1:4]",a[1:4])
print("[0:4:2]",a[0:7:2])
print("[-4:-1]",a[-3:-1])
print("[-3:]",a[-3:])
print("[-3:-2]",a[-3:-5])
print("[-3:-2]",a[-3:-4])
print("[-3:-2]",a[-3:-1])
print("[-3:-2]",a[-3:-2])
print("[1:2]",a[1:2])
a1=a[1:3]
print("a1",a1)
print("a1[0]",a1[0])
p=a1[0]
print("p=a1[0]",p)
print("a1[0][0]",a1[0][0])
for i in p:
    print(i,end=" ")
print("-----------passing List-to function--------------")
d=["Laa","vaa","anya"]
def fun(x):
    print(x)
fun(d)
print("-----------passing and returning List-to function--------------")
d=("Laa","vaa","anya")
def fun(x):
    print(x)
    y=("Lasya","saml")
    return y
z=fun(d)
print(z)
