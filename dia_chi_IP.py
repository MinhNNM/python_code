t=int(input())
for i in range(t):
    s=input()
    st=s.split('.')
    check=1
    for i in st:
        if i>'255':
            check=0
    if check==0 or len(st)<4:
        print("NO")
    else:
        print("YES")