t=int(input())
for k in range(t):
    n=int(input())
    a=[int(i) for i in input().split()]
    dem=1; check=1
    a.sort()
    for i in range(n-1):
        if a[i]==a[i+1]:
            dem+=1
        elif dem%2!=0:
            print(a[i])
            check=0
            break
        else:
            dem=1
    if check:
        print(a[-1])