t=int(input())
for i in range(t):
    n=int(input())
    a=[int(i) for i in input().split()]
    a.sort()
    dem=0
    for i in range(n-1):
        if a[i+1]-a[i]>1:
            dem+=a[i+1]-a[i]-1
    print(dem)