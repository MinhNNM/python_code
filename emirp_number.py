import math
import re
def ngto(n):
    if n<2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
def dao(n):
    s=str(n)
    s1=s[::-1]
    return int(s1)
t=int(input())
for i in range(t):
    n=int(input())
    b=[]
    for i in range(13, n):
        if ngto(i) and ngto(dao(i)) and dao(i)!=i and dao(i)<n:
            b.append(i)
            b.append(dao(i))
    a=[]
    for i in b:
        if i not in a:
            print(i, end=' ')
            a.append(i)
    print()
        