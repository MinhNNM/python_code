a=[int(i) for i in input().split()]
arr=[int(i) for i in input().split()]
arr.sort()
dem=[]
for i in arr:
    dem.append(arr.count(i))
dem.sort(reverse=True)
x=0
for i in dem:
    if i!=dem[0]:
        x=i
        break
for i in arr:
    if arr.count(i)==x:
        print(i)
        break
if dem==0:
    print("NONE")