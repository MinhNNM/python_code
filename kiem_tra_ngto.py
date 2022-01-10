import math
def ngto(n):
    if n<2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
a=[int(i) for i in input().split()]
m=a[0]; n=a[1]
arr=[]
for i in range(m):
    arr.append([int(i) for i in input().split()])
for i in range(m):
    for j in range(n):
        if ngto(arr[i][j]):
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()