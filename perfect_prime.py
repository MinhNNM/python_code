import math
import re
def ngto(n):
    if n<2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
def check(n):
    s=str(n)
    s1=s[::-1]
    if ngto(int(s1)):
        return True
    return False
t=int(input())
for i in range(t):
    n=int(input())
    if ngto(n) and check(n):
        print("Yes")
    else:
        print("No")