import math
def ucln(a, b):
    if b==0:
        return a
    return ucln(b, a%b)
def ngto(n):
    if n<2:
        return False
    x=int(math.sqrt(n))
    for i in range(2, x+1):
        if n%i==0:
            return False
    return True
t=int(input())
for i in range(t):
    a=[int(i) for i in input().split()]
    b=ucln(a[0], a[1])
    s=str(b)
    res=0
    for k in s:
        res+=int(k)
    if ngto(res):
        print("YES")
    else:
        print("NO")
