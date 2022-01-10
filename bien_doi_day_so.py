def check(a):
    for i in range(len(a)-1):
        if a[i]!=a[i+1]:
            return False
    return True
while True:
    a=[int(i) for i in input().split()]
    if a==[0, 0, 0, 0]:
        break
    dem=0
    while not check(a):
        dem+=1
        x=a[0]
        for i in range(3):
            a[i]=abs(a[i]-a[i+1])
        a[3]=abs(a[3]-x)
    print(dem)