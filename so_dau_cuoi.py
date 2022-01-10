t=int(input())
for i in range(t):
    s=input()
    a=s[0]+s[1]
    b=s[-2]+s[-1]
    if a==b:
        print("YES")
    else:
        print("NO")