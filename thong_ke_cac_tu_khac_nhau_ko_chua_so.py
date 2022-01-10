import re
n=int(input())
str=" "
for i in range(n):
    s=input().lower()
    s=s.replace("_", " ")
    s=re.sub("\d", "", s)
    str+=s+" "
a=[]
result={}
list=re.findall(r"[\w']+", str)
for i in list:
    if i not in a:
        a.append(i)
a.sort()
for i in a:
    count=list.count(i)
    result[i]=count
for k, v in sorted(result.items(), key=lambda item:item[1], reverse=True):
    print(k, v)
