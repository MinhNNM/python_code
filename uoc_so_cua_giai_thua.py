def so_ln(n, p):
    x=0
    while(n>0):
        n//=p
        x+=n
    return x
t=int(input())
for k in range(t):
    n, p=[int(i) for i in input().split()]
    print(so_ln(n, p))