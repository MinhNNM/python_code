def add(s, x):
    res=""
    for i in range(x):
        res+=s
    return res
t=int(input())
for i in range(t):
    str=input()
    s1=""
    for k in range(len(str)):
        if str[k]>='1' and str[k]<='9':
            s1=s1+add(str[k-1], int(str[k]))
    print(s1)