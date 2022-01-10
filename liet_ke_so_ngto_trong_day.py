import math
def ngto(n):
    if n<2:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n%i==0:
            return False
    return True
n=int(input())
b=[]
a=[int(i) for i in input().split()]
for i in a:
    if ngto(i) and i not in b:
        b.append(i)
        print(i, a.count(i))
