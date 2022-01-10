t=int(input())
for i in range(t):
    s=input()
    if s[len(s)-1]=='6' and s[len(s)-2]=='8':
        print("YES")
    else:
        print("NO")