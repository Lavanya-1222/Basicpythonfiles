# ------------------List----------------------
print("-------sample list-------")
l=[12,2.4,"kkk"]
print(l)
print("-------empty list-------")
l=[]
print(l)
print("-------Acsseing list-------")
l=[12,2.4,"kkk"]
print(l[0])
print("-------Acsseing list-2------")
l=[12,2.4,"kkk"]
for i in l:
    print(i,end=" ")
print("\n-------Acsseing list-3------")
l=[12,2.4,"kkk"]
for i in range(len(l)):
    print(l[i],end=" ")
print("\n-------modifying list-------")
l=[12,2.4,"kkk"]
l[0]=10

print(l)
print("-------User input list-------")
l1=[]
for  i in range(4):
    l1.append(input())
print(l1)


