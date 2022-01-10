s1=input()
s2=input()
if len(s1)<len(s2):
    s1, s2=s2, s1
while len(s2)<len(s1):
    s2="0"+s2
res=0
tmp=0; s=""
for i in range(len(s1)-1, -1, -1):
    res=int(s1[i])+int(s2[i])+tmp
    if res>9:
        res-=10
        tmp=1
    else:
        tmp=0
    s=str(res)+s
if tmp!=0:
    s="1"+s
dem=0
for i in s:
    if i=='0':
        dem+=1
if dem==len(s):
    s="0"
else:
    s=s.lstrip('0')
print(s)

#c2
# =int(input())
# b=int(input())
# print(a+b)