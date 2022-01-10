n=int(input())
a=input()
arr=a.split(" ")
dem=0
for i in range(n-1):
    for j in range(i+1, n):
        if int (arr[i])>int (arr[j]):
            dem+=1
print(dem)