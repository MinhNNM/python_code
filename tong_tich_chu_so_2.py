t=int(input())
for k in range(t):
    s=input()
    sum=0; res=1; dem=0
    for i in range(len(s)):
        if i%2!=0:
            sum+=int(s[i])
        else:
            if(int(s[i])!=0):
                dem+=1
                res*=int(s[i])
    if dem==0:
        res=0
    print(res, sum)