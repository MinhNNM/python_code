n=int(input())
a=[float(i) for i in input().split()]
b=[]
a.sort()
for i in range(1, len(a)-1):
    if a[i]!=a[0] and a[i]!=a[len(a)-1]:
        b.append(a[i])
sum=0
for i in b:
    sum+=i
print(round(sum/len(b), 2))