import math
def ngto(n):
    if n<2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
x=[int(i) for i in input().split()]
a=[]
for i in range(x[0]):
    a.append([int(i) for i in input().split()])
tmp=0
st=[]
check=0
for i in range(x[0]):
    for j in range(x[1]):
        if ngto(a[i][j]) and a[i][j]>tmp:
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
