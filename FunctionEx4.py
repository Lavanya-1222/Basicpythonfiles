# *******************global***************
print("*******global*********")
x=10
def fun():
   x=1
   x=x+1
   print(x)
fun()
print(x)
print("********gloabl-1********")
x=10
def fun2():
   print(x)
fun2()
def fun():
   global x
   x=x+1
   print(x)
fun()
print(x)
print("********gloabl-2********")
x=10
def fun2():
   print(x)
fun2()
def fun():
   x=20
   y=globals()['x']
   print("Global variable",y)
   x=x+1
   print(x)
fun()
print(x)
print("********gloabl-3*******")
x=10
def fun2():
   print(x)
fun2()
def fun():
   global x
   y=globals()['x']
   print("Global variable",y)
   x=x+1
   print(x)
fun()
print(x)



