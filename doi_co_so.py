gia_tri=[]
for i in range(10):
    gia_tri.append(str(i))
for i in range(10, 36):
    gia_tri.append(chr(i+55))
def chuyen_doi(n, k):
    res=''
    while n!=0:
        res+=gia_tri[n%k]
        n=int(n/k)
    res=res[::-1]
    print(res)
t=int(input())
for k in range(t):
    n, k=[int(i) for i in input().split()]
    chuyen_doi(n, k)