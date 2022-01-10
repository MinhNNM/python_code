t=int(input())
for k in range(t):
    s1=list(input())
    s2=list(input())
    s1.sort(); s2.sort()
    print(f'Test {k+1}:', end=" ")
    if s1==s2:
        print("YES")
    else:
        print("NO")