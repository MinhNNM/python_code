a=[]
while len(a)<10:
    x=[int(i) for i in input().split()]
    a.extend(x)
b=[]; arr=[]
for i in a:
    b.append(i%42)
for i in b:
    if i not in arr:
        arr.append(i)
print(len(arr))