list1 = [1,2,3,4,5]
list2 = [2,3,4,5,6]

for i in range(len(list1)):
    list1[i] = list1[i]*4 +3

ans=[]
for i in range(len(list1)):
    ans.append(list1[i]-list2[i])

sum=0
max=ans[0]
maxn=list1[0]
min=ans[0]
minn=list1[0]
for i in range(len(ans)):
    sum += ans[i]
    if max<ans[i]:
        max = ans[i]
        maxn=list1[i]
    if min>ans[i]:
        min = ans[i]
        minn=list1[i]

print(ans)
print(sum)
print(sum/len(ans))
print(max)
print(maxn)
print(min)
print(minn)
