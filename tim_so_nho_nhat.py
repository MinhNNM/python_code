def so_max(s):
    res=0
    a=[]
    check=1
    for i in s:
        if i>='0' and i<='9':
            res=res*10+int(i)
            check=1
        else:
            if res!=0:
                a.append(res)
            res=0
            check=0
    if check==1:
        a.append(res)
    a.sort()
    return a[0]
t=int(input())
for i in range(t):
    s=input()
    print(so_max(s))