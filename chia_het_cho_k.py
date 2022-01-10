#C1
from math import *
a = [int(i) for i in input().split()]
b = a[2] - a[0]
bd = a[0] // a[1]
jump = 0
if bd*a[1]>=a[0]:
    jump = bd*a[1] - a[0]
else:
    jump = (bd+1)*a[1] - a[0]
kq = []
while jump <= b:
    kq.append(jump)
    jump += a[1]
if len(kq) == 0 or kq[0]==0:
    print(-1)
else:
    print(' '.join([str(i) for i in kq]))
    
 
# C2
a=[int(i) for i in input().split()]
x=a[0]; k=a[1]; n=a[2]
if x>=n or k>n:
    print("-1")
else:
    check=0
    if x>k:
        tmp=k-x%k
    elif x==k:
        tmp=k
    else:
        tmp=k-x
    while tmp+x<=n:
        print(tmp, end=' ')
        tmp+=k
        check=1
    if check==0:
        print('-1')
