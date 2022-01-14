def check(n):
    s=str(n)
    s1=s[::-1]
    check=1
    for i in s:
        if int(i)%2!=0:
            check=0
    if check==1 and s1==s and int(len(s))%2==0:
        return True
    return False
t=int(input())
for i in range(t):
    n=int(input())
    for i in range(22, n, 22):
        if check(i):
            print(i, end=' ')
    print()
