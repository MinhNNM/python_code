t=int(input())
for k in range(t):
    n=int(input())
    sum=0
    if n%2!=0:
        for i in range(1, n+1, 2):
            sum+=1/i
        print('%.6f' % sum)
    else:
        for i in range(2, n+1, 2):
            sum+=1/i
        print("%.6f" % sum)