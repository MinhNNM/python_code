def tong(s):
    sum=0
    for i in s:
        sum+=int(i)
    return sum
t=int(input())
for i in range(t):
    n=int(input())
    s=[int(i) for i in input().split()]
    s.sort(key=lambda x: int(x))
    s.sort(key=lambda y: tong(str(y)))
    for i in s:
        print(i, end=" ")
    print()