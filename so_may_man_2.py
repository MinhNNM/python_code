t=int(input())
for i in range(t):
    dem=0
    s=input()
    for i in range(len(s)):
        if s[i]!='4' and s[i]!='7':
            dem=1
    if dem==0:
        print("YES")
    else:
        print("NO")