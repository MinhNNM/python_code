
import sys
n=int(input())
arr=[int(i) for i in input().split()]
count=sys.maxsize; 
x=arr[0]
for i in range(n):
    dem=0
    for j in range(n):
        dem+=abs(arr[i]-arr[j])
    if dem<count:
        count=dem
        x=arr[i]
print(count, x)