t=int(input())
for k in range(t):
    n=int(input())
    a=[int(i) for i in input().split()]
    b=[int(i) for i in input().split()]
    a.sort()
    b.sort()
    dem=0
    for i in range(n):
        if a[i]>b[i]:
            dem+=1
    if dem==0:
        print("YES")
    else:
        print("NO")