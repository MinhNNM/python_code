import math
def ngto(n):
    if n<2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
s=input().split()
arr=[]
for i in range(int(s[0])):
    arr.append([int(i) for i in input().split()])
max=0
for i in range(int(s[0])):
    for j in range(int(s[1])):
        if ngto(arr[i][j]) and arr[i][j]>max:
            max=arr[i][j]
if max==0:
    print('NOT FOUND')
else:
    print(max)
    for i in range(int(s[0])):
        for j in range(int(s[1])):
            if arr[i][j]==max:
                print(f"Vi tri [{i}][{j}]")
