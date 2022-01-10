def check(s):
    s1=s[::-1]
    if s==s1 and len(s)>1:
        return True
    return False
arr=[]
s=input().split()
for i in range(int(s[0])):
    arr.append([int(i) for i in input().split()])
max=0
for i in range(int(s[0])):
    for j in range(int(s[1])):
        if check(str(arr[i][j])) and arr[i][j]>max:
            max=arr[i][j]
if max==0:
    print("NOT FOUND")
else:
    print(max)
    for i in range(int(s[0])):
        for j in range(int(s[1])):
            if arr[i][j]==max:
                print(f"Vi tri [{i}][{j}]")