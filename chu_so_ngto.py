import math
def ngto(n):
    if n<2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
def check(s):
    dem=0
    for i in s:
        if ngto(int(i)):
            dem+=1
    if len(s)-dem<dem and ngto(len(s)):
        return True
    return False
t=int(input())
for i in range(t):
    s=input()
    if check(s):
        print("YES")
    else:
        print("NO")