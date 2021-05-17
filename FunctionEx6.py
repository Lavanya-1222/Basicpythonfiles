# ----------------PAss by ibject Reference------------
from array import *
print("--------------PAss by object reference-1---------------")
def al(l):
    print(l)
    l.append(55)

    print(id(l))
l=[1,2,34,44]
al(l)
print(l)
print(id(l))
print("--------------Pass by object reference-2---------------")
def al(l):
    print(l)
    print(id(l))
    l=[10,20,30,40]
    print(l)
    print(id(l))
l=[1,2,34,44]
al(l)
print(l)
print(id(l))
print("--------------Passing Array to Function ---------------")
def m(a):
    print(a)
m(array('i',[10,20,30,40]))
print("-------------returning Array to Function ---------------")
def p():
    #print(a)
    return array('u',["l","V"])
s=p()
print(s)
print("-------------Passing and returning Array to Function-3-----------------------------")
def p(a):
    print(a)
    return array('u',["L","V"])
s=p(array('i',[12,232,34,45]))
print(s)