import math
def ngto(n):
    if n<2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
t=int(input())
for k in range(t):
    n=int(input())
    if n==1:
        print(1)
    else:
        s=""
        for i in range(2, int(math.sqrt(n))+1):
            dem=0
            while n%i==0:
                n=int(n/i)
                dem+=1
            if dem>0:
                s+=str(i)
                if dem>0:
                    s+="^"+str(dem)
                if n>dem:
                    s+=" * "
        if ngto(n):
            s+=str(n)+"^1"
        s="1 * "+s
        print(s)