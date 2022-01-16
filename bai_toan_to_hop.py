from itertools import combinations
x=[int(i) for i in input().split()]
a=[int(i) for i in input().split()]
arr=list(set(a))
arr.sort()
for i in combinations(arr, x[1]):
    for k in i:
        print(k, end=' ')
    print()