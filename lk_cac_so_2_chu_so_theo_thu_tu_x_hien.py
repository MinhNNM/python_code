s=input()
arr, a=[], []
for i in range(0, len(s)-1, 2):
    arr.append(int(s[i:i+2]))
for i in arr:
    if i not in a:
        a.append(i)
for i in a:
    print(i, end=" ")