t=int(input())
for i in range(t):
    s=input()
    sum=0
    for i in range(len(s)):
        sum+=int(s[i])
    st=str(sum); st2=""
    for i in range(len(st)-1, -1, -1):
        st2+=st[i]
    if st==st2 and len(st)>1:
        print("YES")
    else:
        print("NO")