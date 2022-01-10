import math
def ngto(n):
    if n<2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
t=int(input())
for k in range(t):
    s=input()
    sum=0
    for i in s:
        sum+=int(i)
    if ngto(sum):
        print("YES")
    else:
        print("NO")