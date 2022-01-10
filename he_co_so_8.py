def chuyen_doi(s):
    res=int(s[0])*4+int(s[1])*2+int(s[2])
    return str(res)
s=input()
r=len(s)%3
if(r>0):
    for i in range(3-r):
        s='0'+s
s1=''; res=''
for i in range(0, len(s)-2, 3):
    s1=s[i:i+3]
    res+=chuyen_doi(s1)
print(res)