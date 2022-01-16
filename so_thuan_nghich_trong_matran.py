import math
def dao(n):
    s=str(n)
    sn=s[::-1]
    if s==sn and len(s)>1:
        return True
    return False
x=[int(i) for i in input().split()]
a=[]
for i in range(x[0]):
    a.append([int(i) for i in input().split()])
tmp=0
st=[]
check=0
for i in range(x[0]):
    for j in range(x[1]):
        if dao(a[i][j]) and a[i][j]>tmp:
            tmp=a[i][j]
for i in range(x[0]):
    for j in range(x[1]):
        if a[i][j]==tmp:
            st.append(i)
            st.append(j)
            check=1
if check==0:
    print("NOT FOUND")
else:
    print(tmp)
    for i in range(0, len(st)-1, 2):
        print(f'Vi tri [{st[i]}][{st[i+1]}]')
