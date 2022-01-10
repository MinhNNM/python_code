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
    dem=0; n=len(s)
    for i in range(len(s)):
        if ngto(int(s[i])):
            dem+=1
    if ngto(n) and dem>int(n/2):
        print("YES")
    else:
        print("NO")