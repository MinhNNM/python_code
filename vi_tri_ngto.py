import math
def ngto(n):
    if n<2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
def check(s):
    for i in range(len(s)):
        if (ngto(i) and not ngto(int(s[i]))) or (not ngto(i) and ngto(int(s[i]))):
            return False
    return True
t=int(input())
for k in range(t):
    s=input()
    if check(s):
        print("YES")
    else:
        print("NO")