a=[]
t=int(input())
for w in range(t):
    a.append(len(input().split()))
i=0
tho=[]
dem=0
while True:
    if a[i]==6:
        tho.append(1)
        dem += 1
        i += 2
        if i>=t:
            break
        while True:
            if a[i]==6:
                i+=2
                if i >= t:
                    break
            else:
                break
    if i>=t:
        break
    if a[i]==7:
        tho.append(2)
        dem += 1
        i += 4
        if i>=t:
            break
        while True:
            if a[i] == 7:
                tho.append(2)
                dem += 1
                i += 4
                if i >= t:
                    break
            else:
                break
    if i>=t:
        break
print(dem)
for i in tho:
    print(i)
