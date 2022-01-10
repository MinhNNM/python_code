t=int(input())
for i in range(t):
    s=input()
    s2=list(s)
    s2.reverse()
    s1= ''.join(s2)
    dem=0
    for i in range(1, len(s)-1):
        if abs(ord(s[i])-ord(s[i-1]))!=abs(ord(s2[i])-ord(s2[i-1])):
            dem=1
    if dem==0:
        print("YES")
    else:
        print("NO")