t=int(input())
a=[0, 3, 5, 7, 10, 13, 16, 20, 23, 27,
    30, 33, 35, 37, 39]
b=[0.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 
    6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0]
for k in range(t):
    s=input().split()
    d1=int(s[0])
    d2=int(s[1])
    d3=float(s[2])
    d4=float(s[3])
    for i in range(len(a)):
        if d1>a[i]:
            l=b[i]
        else:
            break
    for i in range(len(a)):
        if d2>a[i]:
            r=b[i]
        else:
            break
    tong=(r+l+d3+d4)/4
    if tong-int(tong)<0.25:
        print(float(int(tong)))
    elif tong-int(tong)<0.75:
        print(int(tong)+0.5)
    else:
        print(int(tong)+1.0)