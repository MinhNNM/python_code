t = int(input())
for k in range (t):
    lq = int(input())
    a = []
    while lq > 0:
        so = int(input())
        a.append(so)
        lq -= 1
    a.sort()
    max = 0
    kq = 0
    dem = 1
    for i in range(1,len(a)):
        if a[i] == a[i-1]:
            dem += 1
        elif dem > max:
            max = dem
            kq = a[i-1]
            dem = 1
        else:
            dem = 1
    if dem > max:
        kq = a[len(a)-1]
    print(kq)