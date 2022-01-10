n=int(input())
a=[]
while len(a) < n:
    x = [int(i) for i in input().split()]
    a.extend(x)
chan=[]; le=[]
for i in range(n):
    if a[i]%2==0:
        chan.append(a[i])
        a[i]=-1
    else:
        le.append(a[i])
        a[i]=-2
chan.sort(); le.sort(reverse=True)
for i in range(n):
    if a[i]==-1:
        a[i]=chan[0]
        chan.pop(0)
    elif a[i]==-2:
        a[i]=le[0]
        le.pop(0)
print(' '.join(str(i) for i in a))