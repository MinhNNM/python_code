n=int(input())
arr=[]
for i in range(n):
    arr.append([int(i) for i in input().split()])
k=int(input())
sum, s1, x=0, 0, 0
for i in range(n):
    for j in range(n):
        sum+=arr[i][j]
        if i+j<n-1:
            s1+=arr[i][j]
        if i+j==n-1:
            x+=arr[i][j]
s2=sum-s1-x
if abs(s1-s2)<=k:
    print("YES")
    print(abs(s1-s2))
else:
    print("NO")
    print(abs(s1-s2))