x=[int(i) for i in input().split()]
a=[]
b=[]
for i in range(x[0]):
    st=[int(i) for i in input().split()]
    a.append([int(i) for i in st])
    b.extend([int(i) for i in st])
check=0
s=[]
tp=max(b)-min(b)
for i in range(x[0]):
    for j in range(x[1]):
        if a[i][j]==tp:
            s.append(i)
            s.append(j)
            tmp=a[i][j]
            check=1
if check==0:
    print("NOT FOUND")
else:
    print(tmp)
    for i in range(0, len(s)-1, 2):
        print(f'Vi tri [{s[i]}][{s[i+1]}]')