arr=[int(i) for i in input().split()]
a, b=arr[0], arr[1]
x=set([int(i) for i in input().split()])
y=set([int(i) for i in input().split()])
giao=[int(i) for i in x if i in y]
hieu1=[int(i) for i in x if i not in y]
hieu2=[int(i) for i in y if i not in x]
giao.sort(); hieu1.sort(); hieu2.sort()
for i in giao:
    print(i, end=" ")
print()
for i in hieu1:    
    print(i, end=" ")
print()
for i in hieu2:
    print(i, end=" ")
