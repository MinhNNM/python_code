def tang(s):
    for i in range(len(s)-1):
        if int(s[i+1])-int(s[i])<=0:
            return False
    return True
def giam(s):
    for i in range(len(s)-1):
        if int(s[i])-int(s[i+1])<=0:
            return False
    return True
t=int(input())
for i in range(t):
    s=input()
    check=0
    
    for i in range(len(s)):
        if tang(s[:i]) and giam(s[i::]):
            check=1
    if check==1 and len(s)>=3:
        print("YES")
    else:
        print("NO")