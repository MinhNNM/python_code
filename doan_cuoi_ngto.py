import math
def ngto(n):
    if n<2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
def check(s):
    sum=0
    for i in range(-4, 0):
        sum=sum*10+int(s[i])
    if ngto(sum):
        return True
    return False
t=int(input())
for k in range(t):
    s=input()
    if check(s):
        print("YES")
    else:
        print("NO")