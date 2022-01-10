s1=input()
s=""; s2=""
for i in range(len(s1)-1, -1, -1):
    s2+=s1[i]
for i in range(len(s1)-1, -1, -1):
    s+=s2[i]
    if i%3==0 and i!=0:
        s+=","
print(s)
