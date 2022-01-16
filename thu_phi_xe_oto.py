t=int(input())
a=[2, 5, 7, 29, 45]
b=[20000, 10000, 15000, 50000, 70000]
dic={}
for k in range(t):
    s=input().split()
    if s[-1] in dic and s[-2]=='IN':
        dic[s[-1]]=dic[s[-1]]+b[a.index(int(s[2]))]
    if s[-1] not in dic and s[-2]=='IN':
        dic[s[-1]]=b[a.index(int(s[2]))]
for k, v in dic.items():
    print(f'{k}: {v}')