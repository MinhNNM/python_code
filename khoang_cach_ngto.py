import math
def ngto(n):
    if n<2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
a=[int(i) for i in input().split()]
n=a[0]; x=a[1]
i=2; b=[]
while n>0:
    if ngto(i):
        b.append(i)
        n-=1
    i+=1
print(x, end=" ")
for i in b:
    x+=i
    print(x, end=" ")