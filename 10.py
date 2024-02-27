import random

list1=[random.uniform(0,1) for i in range(10)]
list2=[list1[i]*0.2 for i in range(10)]
list3=[list1[i]-list2[i] for i in range(10)]

print(list1)
print(list2)
print(list3)