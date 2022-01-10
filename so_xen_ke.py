def check(s):
    for i in range(0, len(s)-1):
        if s[i]!=s[i+1]:
            return False
    return True
t=int(input())
for k in range(t):
    s=input()
    s1=""
    for i in range(0, len(s), 2):
        s1+=s[i]
    if check(s1) and len(s)%2!=0 and (int(s[0])!=int(s[1])):
        print("YES")
    else:
        print("NO")