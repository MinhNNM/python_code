t=int(input())
for i in range(t):
    n=[int(i) for i in input().split()]
    a=[int(i) for i in input().split()]
    b=max(a)
    for i in range(n[0]):
        if a[i]==b:
            index=i
            break
    a.insert(index, n[1])
    dem=0
    for i in range(len(a)-1):
        if a[i]<0:
            a.insert(dem, a[i])
            a.pop(i+1)
            dem+=1
    if a[len(a)-1]<0:
        a.insert(dem, a[len(a)-1])
        a.pop(len(a)-1)
    for i in a:
        print(i, end=' ')
    print()