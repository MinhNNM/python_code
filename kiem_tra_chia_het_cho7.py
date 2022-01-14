def tong(n):
    s=str(n)
    s1=s[::-1]
    return int(s)+int(s1)
t=int(input())
for i in range(t):
    n=int(input())
    dem=0
    while n%7!=0 and dem<=1000:   
        n=tong(n)
        dem+=1
    print(n)
