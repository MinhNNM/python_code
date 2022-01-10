import math
def ucln(a, b):
    if b==0:
        return a
    return ucln(b, a%b)
def so_dao(n):
    s=str(n); res=0
    for i in range(len(s)-1, -1, -1):
        res=res*10+int(s[i])
    if ucln(res, n)==1:
        return True
    else:
        return False
t=int(input())
for k in range(t):
    n=int(input())
    if so_dao(n):
        print("YES")
    else:
        print("NO")
    