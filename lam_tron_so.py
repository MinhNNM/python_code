t = int(input())
for x in range (t):
    n = input()
    n = list(n)
    memory = 0
    for i in range(-1, -1-len(n), -1):
        n[i] = int(n[i]) + memory
        if i != -len(n):
            if n[i] >= 5:
                n[i] = 0
                memory = 1
            else:
                n[i] = 0
                memory = 0

    print(''.join([str(i) for i in n]))