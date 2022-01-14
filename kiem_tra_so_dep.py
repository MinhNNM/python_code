def check(s):
    check=1
    for i in range(len(s)-2):
        if s[i]!=s[i+2]:
            check=0
    if check==1 and len(set(s))==2:
        return True
    return False
t=int(input())
for i in range(t):
    s=input()
    if check(s):
        print("YES")
    else:
        print("NO")