# -----------------Tuple-----------------------
print("-------------------Creating empty tuple----------------")
t=()
print(t)
print("-------------------Creating one element----------------")
t=(10)
print(type(t),t)
t=(10,)
print(type(t),t)
print("-------------------creating sample  tuple----------------")
t=(12,13,14,15)
print(t)
print("-------------------Assecting tuple----------------")
t=(10,20,30,40)
print(t[1])
print("-------------------Assecting tuple with loop---------------")
t=(10,20,30,40)
print("without index")
for i in t:
    print(i,end=" ")
print()
print("with index")
for i in range(len(t)):
    print(t[i],end=" ")
print()
print("while loop")
i=0
while i<len(t):
    print(t[i],end=" ")
    i+=1