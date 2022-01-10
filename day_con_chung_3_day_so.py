n=int(input())
for t in range(n):
    x=[int(i) for i in input().split()]
    a=[int(i) for i in input().split()]
    b=[int(i) for i in input().split()]
    c=[int(i) for i in input().split()]
    i = j = k = dem = 0
    while i<len(a) and j<len(b) and k<len(c):
        if(a[i]==b[j] and b[j]==c[k]):
            print(a[i], end=" ")
            dem=1
            i+=1; j+=1; k+=1
        elif a[i]<b[j]:
            i+=1
        elif b[j]<c[k]:
            j+=1
        else:
            k+=1
    if dem==0:
        print("NO", end=" ")
    print()