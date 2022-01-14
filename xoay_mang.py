t=int(input())
while t>0:
    x=[int(j) for j in input().split()]
    a=[int(k) for k in input().split()]
    for i in range(x[1], x[0]):
        print(a[i], end=' ')
    for i in range(x[1]):
        print(a[i], end=' ')
    print()
    t-=1
