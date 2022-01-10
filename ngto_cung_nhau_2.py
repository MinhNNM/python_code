import math
def ucln(a, b):
    if b==0:
        return a
    return ucln(b, a%b)
arr=[int(i) for i in input().split()]
a, b=arr[0], arr[1]
n, m=pow(10, b-1), pow(10, b)
s=[]
for i in range(n, m):
        if ucln(i, a)==1:
            s.append(i)
x, leng=0, 10
while leng<=len(s):
    for i in range(x, leng):
        print(s[i], end=' ')
    print()
    leng+=10;x+=10
if len(s)<leng:
    for i in range(leng-10, len(s)):
        print(s[i], end=" ")
    