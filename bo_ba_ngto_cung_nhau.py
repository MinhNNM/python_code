def gcd(a,b):
	while b!=0:
		tmp=a%b
		a=b
		b=tmp
	return a
(a, b)=[int(i) for i in input().split()]
arr=[]
for i in range(a, b-1):
    for j in range(i+1, b+1):
        if gcd(i, j)==1:
            arr.append(j)
    for j in range(len(arr)-1):
        for k in range(j+1, len(arr)):
            if gcd(arr[j], arr[k])==1:
                print(f'({i}, {arr[j]}, {arr[k]})')
    arr.clear()