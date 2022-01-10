def fibo(n):
    f1=0; f2=1
    if n==1:
        return 1
    for i in range(2, n+1):
        f=f1+f2
        f1=f2
        f2=f
    return f
t=int(input())
for i in range(t):
    x=[int(i) for i in input().split()]
    a=x[0]
    b=x[1]
    for i in range(a, b+1):
        print(fibo(i), end=" ")
    print()