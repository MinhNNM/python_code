import math
def ngto(n):
    if n<2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
def check(s):
    sum=0; sum2=0
    for i in range(-3, 0):
        sum=sum*10+int(s[i])
    for i in range(0, 3):
        sum2=sum2*10+int(s[i])
    if ngto(sum) and ngto(sum2):
        return True
    return False
t=int(input())
for k in range(t):
    s=input()
    if check(s):
        print("YES")
    else:
        print("NO")