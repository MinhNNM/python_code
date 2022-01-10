arr=[]
s=input().split()
for i in range(int(s[0])):
    arr.append([int(i) for i in input().split()])
max=0; dem=0
min=10005
for i in range(int(s[0])):
    for j in range(int(s[1])):
        if arr[i][j]>max:
            max=arr[i][j]
        if arr[i][j]<min:
            min=arr[i][j]
for i in range(int(s[0])):
    for j in range(int(s[1])):
        if arr[i][j]==max-min:
            dem=1
if dem==0:
    print("NOT FOUND")
else:
    print(max-min)
    for i in range(int(s[0])):
        for j in range(int(s[1])):
            if arr[i][j]==max-min:
                print(f"Vi tri [{i}][{j}]")