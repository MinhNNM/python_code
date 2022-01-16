from math import comb


def giaithua(n):
    gt = 1
    for i in range(1,n+1):
        gt*=i
    return gt
def tohop(k, n):
    return int(giaithua(n) / (giaithua(k)*giaithua(n-k)))
n = int(input())
a = []
for i in range(n):
    s = input()
    a.append(s)
kq = 0
for i in range(n):
    dem = 0; dem1=0
    for j in range(n):
        if a[i][j] == 'C':
            dem += 1
        if a[j][i] == 'C':
            dem1 += 1
    kq = kq + tohop(2,dem) + tohop(2, dem1) 
print(kq)