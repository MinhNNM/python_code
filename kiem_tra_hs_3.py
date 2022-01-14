def check(s):
    for i in s:
        if i!='0' and i!='2' and i!='1':
            return False
    return True
t=int(input())
for i in range(t):
    s=input()
    if check(s):
        print("YES")
    else:
        print("NO")