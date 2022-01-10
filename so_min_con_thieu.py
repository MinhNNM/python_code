n=int(input())
a=[int(i) for i in input().split()]
a.sort()
x=0; dem=0
for i in range(len(a)-1):
    if a[i+1]-a[i]>1:
        x=a[i]+1
        dem=1
        break
if dem==1:
    print(x)
else:
    print(a[n-1]+1)
