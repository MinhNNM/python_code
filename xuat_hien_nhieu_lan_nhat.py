t=int(input())
for i in range(t):
    n=int(input())
    a=[int(i) for i in input().split()]
    a.sort()
    dem=1; max=1; res=a[0]
    for i in range(1, n):
        if (a[i]==a[i-1]):
            dem+=1
        else:
            if dem>max:
                max=dem
                res=a[i-1]
            dem=1
    if dem>max:
        max=dem
        res=a[n-1]
    if max>n/2:
        print(res)
    else:
        print("NO")

