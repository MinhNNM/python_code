P="ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
def check(s):
    for i in range(len(P)):
        if P[i]==s:
            return i
while True:
    s=input()
    a=s.split()
    if s=='0':
        break
    else:        
        k=int(a[0])
        s2=""
        s1=a[1]
        for i in range(len(s1)):
            s2=P[(check(s1[i])+k)%28]+s2
        print(s2) 