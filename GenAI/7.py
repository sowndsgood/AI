arr=[]
for i in range(5):
    col=[]
    for j in range(5):
        col.append(j)
    arr.append(col)

print(arr)

arr1=[]
for i in range(5):
    col1=[]
    for j in range(5):
        col1.append(arr[i][j]+10)
    arr1.append(col1)




print(arr1)
