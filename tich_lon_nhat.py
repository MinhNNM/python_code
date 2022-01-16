n=int(input())
a=[int(i) for i in input().split()]
a.sort()
print(max(a[0]*a[1]*a[-1], a[-1]*a[-2]*a[-3]))