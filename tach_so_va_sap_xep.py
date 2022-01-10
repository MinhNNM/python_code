t=int(input())
a=[]
for k in range(t):
    sum=0; dem=0
    s=input()
    for i in s:
        if i.isdigit():
            sum=sum*10+int(i)
            dem=1
        else:
            if(dem==1):
                a.append(sum)
                dem=0
            sum=0
    if(dem==1):
        a.append(sum)
a.sort()
for i in a:
    print(i) 