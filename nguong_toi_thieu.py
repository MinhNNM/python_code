s=input()
k=int(input())
arr, a=[], []
for i in range(0, len(s)-1, 2):
    arr.append(int(s[i:i+2]))
for i in arr:
    if i not in a:
        a.append(i)
a.sort(); dem=0
for i in a:
    if arr.count(i)>=k:
        print(i, arr.count(i))
        dem=1
if dem==0:
    print("NOT FOUND")