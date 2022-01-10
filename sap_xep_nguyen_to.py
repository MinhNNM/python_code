import math
def ngto(n):
    if n<2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
n=int(input())
arr=[int(i) for i in input().split()]
a=[]
for i in arr:
    if ngto(i):
        a.append(i)
a.sort()
for i in range(n):
    if ngto(arr[i]):
        arr[i]=a[0]
        a.pop(0)
for i in arr:
    print(i, end=" ")