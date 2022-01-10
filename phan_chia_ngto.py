import math
def ngto(n):
    if n<2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
n=int(input())
a=[int(i) for i in input().split()]
b=[]; sum=[]; check=False
for i in a:
    if i not in b:
        b.append(i)
sum.append(b[0])
for i in range(1,len(b)):
    sum.append(b[i]+sum[i-1])
for i in range(len(b)):
    if ngto(sum[i]) and ngto(sum[len(b)-1]-sum[i]):
        check=True
        print(i)
        break
if check==False:
    print("NOT FOUND")