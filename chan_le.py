def check(x):
    for i in range(len(x)-2):
        if abs(int(s[i+1])-int(s[i]))!=2:
            return False
    return True
t=int(input())
for i in range(t):
    s=input()
    res=0
    for i in s:
        res+=int(i)
    if res%10==0 and check(s):
        print("YES")
    else:
        print("NO")