import math
def ucln(a, b):
    if b==0:
        return a
    return ucln(b, a%b)
n=int(input())
a=[int(i) for i in input().split()]
a.sort()
for i in range(n-1):
    for j in range(i+1, n):
        if ucln(a[i], a[j])==1:
            print(a[i], a[j])