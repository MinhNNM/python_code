t=int(input())
for k in range(t):
    s=input()
    res=1
    for i in s:
        if int(i)!=0:
            res*=int(i)
    print(res)
