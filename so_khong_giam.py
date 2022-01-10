t=int(input())
for k in range(t):
    s=input()
    dem=0
    for i in range(len(s)-1):
        if s[i+1]<s[i]:
            dem=1
    if dem==0:
        print("YES")
    else:
        print("NO")