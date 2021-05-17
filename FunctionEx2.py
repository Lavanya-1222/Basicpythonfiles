# *****************function types of Arguments ***************
print("--------positional order---------")
def fun(x,y):
     print(x**y)
fun(5,2)
fun(2,5)
print("--------keyword Arguments-1--------")
def fun1(name="Lava",age="20"):
    print(name,age)
fun1()
print("--------keyword Arguments-2--------")
def fun2(name,age):
    print(name,age)
fun2(name="Lavanya",age="20")
print("--------keyword Arguments-3--------")
def fun3(age,name):
    print(name,age)
fun3(name="Lava",age=20)
print("--------keyword Arguments-4--------")
def fun3(age,name):
    print(name,age)
fun3("Lava",20)
print("--------Default Arguments--------")
def fun4(name,age=20):
    print(name,age)
fun4(name="Lavanya")
print("--------Default Arguments-2-------")
def fun4(name,age=20):
    print(name,age)
fun4(name="Lavanya",age=21)
print("--------Variable Length Argument---------")
def fun5(*nam):
    print(nam[0],nam[1])
fun5("lavanya","Samarth")
print("--------Variable Length Argument-2--------")
def fun5(*nam):
    name="Lava"
    print(name,nam[0],nam[1])
fun5("lavanya","Samarth")
print("--------keyword variable length arguments--------")
def fun7(**num):
    print(num['a'],num['b'],num['c'])
fun7(a="Lavanya",b="Samarth",c="M")

