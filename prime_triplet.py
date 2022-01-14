import math
def ngto(n):
    if n<2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
t=int(input())
for i in range(t):
    n=int(input())
    dem=0
    for i in range(5, n-6, 2):
        if ngto(i) and ngto(i+2) and ngto(i+6) or ngto(i) and ngto(i+4) and ngto(i+6):
            dem+=1
    print(dem)