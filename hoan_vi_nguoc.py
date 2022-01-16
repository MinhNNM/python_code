from itertools import permutations
def gt(n):
    res=1
    for i in range(1, n+1):
        res*=i
    return res
t=int(input())
for i in range(t):
    n=int(input())
    s=''
    print(gt(n))
    for i in range(n, 0, -1):
        s+=str(i)
    for i in permutations(s):
        print(''.join(i), end=' ')
    print()