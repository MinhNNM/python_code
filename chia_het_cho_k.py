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