import re
n=int(input())
a=[]; str=""
for i in range(n):
    s=input().lower()
    str+=s+" "
list=re.findall(r"[\w']+", str)
for i in list:
    if i not in a:
        a.append(i)
result={}
a.sort()
for word in a:
    count = list.count(word)
    result[word]=count
for k, v in sorted(result.items(), key=lambda item: item[1], reverse=True):
    print(k, v)