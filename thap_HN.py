def thap_HN(n, A, B, C):
    if n==1:
        print(f'{A} -> {C}')
    else:
        thap_HN(n-1, A, C, B)
        print(f'{A} -> {C}')
        thap_HN(n-1, B, A, C)
n=int(input())
thap_HN(n, 'A', 'B', 'C')