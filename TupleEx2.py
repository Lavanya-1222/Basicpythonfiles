# -----------------Slicing on tuple-------------------
a=(10,20,30,40,50,60,70)
print("[1:5]",a[1:5])
print("[0:]",a[0:])
print("[-4:]",a[-4:])
print("[-4:-3]",a[-4:-3])
print("[-4:-8]",a[-4:-8])
print("[-4:-5]",a[-4:-5])
print("[-4:-1]",a[-4:-1])
print("[0:7:2]",a[0:7:2])
print("-------------------Tuple Concatenation----------------")
t=(10,20,30,40)
p=(1,1,1,1)
print(t+p)
print("-------------------Modifying ele----------------")
t=(10,20,30,40)
# t[1]=10
print("TypeError: 'tuple' object does not support item assignment")
print("-------------------Tuple Repetition----------------")
t=(10,20,30,40)
print(t*2)
print("-------------------deleting Tuple----------------")
a=(10,20,30,40)
del a
print("NameError: name 'a' is not defined")
print("-------------------Alision Tuple----------------")
a=(10,20,30,40)
b=a
print(a,id(a))
print(b,id(b))

print("a[0]=10 TypeError: 'tuple' object does not support item assignment")
print("-------------------copying Tuple----------------")
a=(10,20,30,40)
b=a[0:]
print(a,id(a))
print(b,id(b))
print("-------------------user input Tuple----------------")
a=[]
for i in range(5):
    a.append(int(input()))

print(tuple(a))