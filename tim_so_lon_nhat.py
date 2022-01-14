def so_max(s):
    res=0
    a=[]
    for i in s:
        if i>='0' and i<='9':
            res=res*10+int(i)
        else:
            res=0
        a.append(res)
    a.sort()
    return a[len(a)-1]
t=int(input())
for i in range(t):
    s=input()
    print(so_max(s))