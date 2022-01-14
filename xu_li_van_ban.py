import re
s=""
while True:
    n=input()
    s+=n+" "
    if n[-1]=='.':
        break
st=re.split('\.|\!|\?', s)
for i in st:
    i=i.title().strip()
    x=re.split('\\s+', i)
    for j in range(len(x)):
        if j==0:
            print(x[j], end=' ')
        else:
            print(x[j].lower(), end=' ')
    print()