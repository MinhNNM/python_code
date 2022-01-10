def check(s):
    sum=0
    for i in s:
        sum+=int(i)
    if sum%3==0:
        return True
    return False
t=int(input())
for k in range(t):
    s=input()
    if check(s):
        print("YES")
    else:
        print("NO")
