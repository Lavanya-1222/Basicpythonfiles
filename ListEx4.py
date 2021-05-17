# ------------------Nested List---------------------
b=[50,60]
a=[10,20,30,b]
print(a)
print("-----------Accessing Nested List---------------")
print(a[3][0])
print(a[3][1])
print("-----------Modifying  Nested List---------------")
a[3][0]=100
print(a[3][0])
print(a)
a[3][0]=50
print(a)
print("-----------Accessing Nested List using loop---------------")
print("without index")
for i in a:
    if type(i) is list:
        for j in i:
            print(j,end=" ")
    else:
        print(i,end=" ")
print()
print("with index")
for i in range(len(a)):
    if type(a[i]) is list:
        for j in range(len(a[i])):
            print(a[i][j],end=" ")
    else:
        print(a[i],end=" ")
print()
print("while loop")
i=0
while i<len(a):
    if type(a[i]) is list:
        j=0
        while j<len(a[i]):
            print(a[i][j],end=" ")
            j+=1
        i+=1
    else:
        print(a[i],end=" ")
        i+=1
print()
print("-----------Nested List-2--------------")
c=[[10,20,30],[40,50,60]]
print(c)
print("-----------Accessing Nested List---------------")
print(c[0][2])
print(c[1][2])
print("-----------Accessing Nested List using loop---------------")
print("without index")
for i in c:
    for j in i:
        print(j,end=" ")
print()
print("with index")
for i in range(len(c)):
    for j in range(len(c[i])):
        print(c[i][j],end=" ")
print()
print("while loop")
i=0
while i<len(c):
    j=0
    while j<len(c[i]):
        print(c[i][j],end=" ")
        j+=1
    i+=1
print()
print("-----------passing List-to function--------------")
d=["Laa","vaa","anya"]
def fun(x):
    print(x)
fun(d)
print("-----------passing and returning List-to function--------------")
d=["Laa","vaa","anya"]
def fun(x):
    print(x)
    y=["Lasya","saml"]
    return y
z=fun(d)
print(z)
print("----------------------------------Slicing Nested List----------------------------------")
a=[[10,20,30],[40,50,60],[70,80,90],[11,22,33]]
print("a[0:]",a[0:])
print("a[1:4]",a[1:4])
print("[0:4:2]",a[0:7:2])
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
print("-----------------------Tuple of lists-------------------")
a=(10,20,[30,40])
print(a)
print("-----------------------Accessing Tuple of lists-------------------")
print(a[2][0])
print("without index")
for i in range(len(a)):
    if type(a[i]) is list:
        for j in range(len(a[i])):
            print(a[i][j],end=" ")
    else:
        print(a[i],end=" ")
print("\nwhile loop")
i=0
while i<len(a):
    j=0
    if type(a[i]) is list:
      while j<len(a[i]):
        print(a[i][j],end=" ")
        j+=1
    else:
        print(a[i],end=" ")
    i+=1
print("\n-----------------------Modifying Tuple of lists-------------------")
a[2][0]=90
print(a)
print()
print("-----------------------Tuple of lists-2------------------")
a=([10,20],[30,40])
print(a)
print("-----------------------Accessing Tuple of lists-------------------")
print(a[1][0])
print("For loop")
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j],end=" ")
print("\nwhile loop")
i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        print(a[i][j],end=" ")
        j+=1
    i+=1
print("\n-----------------------Modifying Tuple of lists-------------------")
a[0][1]=90
print(a)
print()
print()
print("-----------------------lists of tuples-------------------")
a=[10,20,(30,40)]
print(a)
print("-----------------------Accessing lists of tuples-------------------")
print(a[2][0])
print("without index")
for i in range(len(a)):
    if type(a[i]) is list:
        for j in range(len(a[i])):
            print(a[i][j],end=" ")
    else:
        print(a[i],end=" ")
print("\nwhile loop")
i=0
while i<len(a):
    j=0
    if type(a[i]) is list:
      while j<len(a[i]):
        print(a[i][j],end=" ")
        j+=1
    else:
        print(a[i],end=" ")
    i+=1
print("\n-----------------------Modifying lists of tuples-------------------")
a[0]=9000
print(a)
a[0]=10
print("\n-----------------------lists of tuples-1------------------")
a=[(10,20),(30,40)]
print(a)
print("-----------------------Accessing lists of tuples-------------------")
print(a[1][0])
print("For loop")
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j],end=" ")
print("\nwhile loop")
i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        print(a[i][j],end=" ")
        j+=1
    i+=1

print("\n-----------------------Modifying lists of tuples-------------------")

print("a[0][0]=90 TypeError: 'tuple' object does not support item assignment ")

