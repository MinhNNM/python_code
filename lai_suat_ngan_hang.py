t=int(input())
for i in range(t):
     a=[float(i) for i in input().split()]
     x=a[0]+a[0]*a[1]/100
     b=a[1]/100
     dem=1
     while x<=a[2]:
          x+=x*b
          dem+=1
     print(dem)