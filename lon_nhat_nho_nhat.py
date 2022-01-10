while(True):
    n=int(input())
    arr=[]
    if n==0:
        break;
    else:
        for i in range(n):
            x=int(input())
            arr.append(x)
        arr.sort(); y=len(arr)
        if arr[0]==arr[y-1]:
            print("BANG NHAU")
        else:
            print(arr[0], arr[y-1])
