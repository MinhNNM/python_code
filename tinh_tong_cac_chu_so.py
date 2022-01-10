t=int(input())
for k in range(t):
    s=input()
    res=0; s1=""
    for i in s:
        if i>='0' and i<='9':
            res+=int(i)
        else:
            s1+=i
    x=sorted(s1)
    y=''.join(x)
    print(y + str(res))