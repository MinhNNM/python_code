n=int(input())
a=[]
check=1
while len(a)<n:
    a.extend([int(i) for i in input().split()]) 
if a[0]>1:
    for j in range(1,a[0]):
        check=0
        print(j)
for i in range(n-1):
    if a[i+1]-a[i]>1:
        for j in range(a[i]+1, a[i+1]):
            print(j)
            check=0
if check==1:
    print("Excellent!")