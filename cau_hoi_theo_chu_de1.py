t=int(input())
x=[]
tmp=0
a=[]
for i in range(t):
    x.append(input())
for i in range(len(x)):
    if x[i]=='':
        print(f'{x[tmp]}: {i-tmp-1}')
        tmp=i+1
print(f'{x[tmp]}: {len(x)-tmp-1}')