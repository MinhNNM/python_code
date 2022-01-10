import re
str=""
x=[int(i) for i in input().split()]
for i in range(x[0]):
    s=input().lower()
    s=s.replace("_", " ")
    str+=s+" "
a=[]
list=re.findall(r"[\w']+", str)
for i in list:
    if i not in a:
        a.append(i)
a.sort()
result={}
for i in a:
    count=list.count(i)
    if count>=x[1]:
        result[i]=count
for k, v in sorted(result.items(), key=lambda item: item[1], reverse=True):
    print(k, v)