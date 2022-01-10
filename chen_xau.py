s1=input()
s2=input()
x=int(input())
s=""
for i in range(x-1):
    s+=s1[i]
s+=s2
for i in range(x-1, len(s1)):
    s+=s1[i]
print(s)