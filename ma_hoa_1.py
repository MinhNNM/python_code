t=int(input())
for k in range(t):
    s=input()
    x=0; res=""
    for i in range(1, len(s)):
        if s[i]!=s[x]:
            res+=str(i-x)+s[x]
            x=i
    res+=str(len(s)-x)+s[x]
    print(res)