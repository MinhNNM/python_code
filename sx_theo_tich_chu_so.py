def tich(s):
    res=1
    for i in s:
        res*=int(i)
    return res
t=int(input())
for k in range(t):
    n=int(input())
    s=[int(i) for i in input().split()]
    s.sort(key=lambda x: x)
    s.sort(key=lambda x: tich(str(x)))
    for i in s:
        print(i, end=" ")
    print()