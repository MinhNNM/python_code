from math import e


n, m=[int(i) for i in input().split()]
a=[]
for i in range(n):
    a.append([int(i) for i in input().split()])
if n>m:
    i=0
    while n>m:
        del a[i]
        i+=1; n-=1
else:
    i=1
    while n<m:
        for k in range(n):
            del a[k][i]
        i+=1; m-=1
for i in range(n):
    for j in range(m):
        print(a[i][j], end=' ')
    print()