def ucln(a, b):
    if b==0:
        return a
    return ucln(b, a%b)
t=int(input())
for i in range(t):
    a=int(input())
    b=int(input())
    print(ucln(a, b))