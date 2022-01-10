import math
def ucln(a, b):
    if b==0:
        return a
    return ucln(b, a%b)
def ngto(n):
    if n<2:
        return False
    m=int(math.sqrt(n))
    for i in range(2, m+1):
        if n%i==0:
            return False
    return True
t=int(input())
for i in range(t):
    n=int(input())
    dem=0
    for i in range(1,n):
        if ucln(i, n)==1:
            dem+=1
    if ngto(dem):
        print("YES")
    else:
        print("NO")