s=input()
sum=0
while(len(s)>1):
    s1=s[0:int(len(s)/2)]
    s2=s[int(len(s)/2): len(s)]
    sum1, sum2=0, 0
    for i in s1:
        sum1=sum1*10+int(i)
    for i in s2:
        sum2=sum2*10+int(i)
    sum=sum1+sum2
    s=str(sum)
    print(s)
