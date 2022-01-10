s=input().split()
a=set([int(i) for i in input().split()])
b=set([int(i) for i in input().split()])
A=[int(i) for i in a]
B=[int(i) for i in b]
A.sort(); B.sort()
if len(A)!=len(B):
    print("NO")
else:
    dem=0
    for i in range(len(A)):
        if A[i]==B[i]:
            dem+=1
    if dem==0:
        print("NO")
    else:
        print("YES")