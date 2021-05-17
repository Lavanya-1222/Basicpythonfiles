# *****************function***************
def fun(x,y):
    print(x+y)
print("Function with 2 arg and print")
fun(10,20)
def fun1(x,y):
    return x+y
print("funtion with single arg return")
x=fun1(10,20)
print(x)
print("----------------funtion with 2 arg return------------------")
fun1(10,20)
def fun3(x,y):
    return (x+y),(x-y)
add,sub=fun3(10,20)
print("addition",add,"\nsubstraction",sub)
print("---------Nested functon------------")
def fun3():
    def inner():
        print("This is inner functon")
    print("this is the outer fun")
    inner()
fun3()
print("---------Nested functon with return------------")
def fun4():
    def inner2():
        return "This is inner fun"

    print(inner2())
    return "This is the outer fun"

t=fun4()
print(t)
print("--------Passing funtion as parameter------------")
def fun5(f):
    print("This fun accept the fun as parameter")
    print(f())
def fun6():
    print("this is passing as parameter")
    return 20
fun5(fun6)
print("--------funtion return another fun------------")
def fun7(f):
    print("This functon returning another fun")
    return f
def fun8():
    print("this is function used to pass and return")
s=fun7(fun8)
s()
print("--------funtion return another fun-2-----------")
def fun9():
    print("This fun returns another fun")
    def fun10():
        print("This is fun ")
    return fun10
s=fun9()
s()