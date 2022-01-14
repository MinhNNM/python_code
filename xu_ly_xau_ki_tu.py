st1=input().lower().split(" ")
st2=input().lower().split(" ")
s=[]; x=[]
for i in st1:
    if i not in s:
        s.append(i)
for i in st2:
    if i not in s:
        s.append(i)
    if i in st1 and i not in x:
        x.append(i)
s.sort()
x.sort()
print(' '.join(s))
print(' '.join(x))