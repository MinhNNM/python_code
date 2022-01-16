from itertools import permutations
s=input()
for i in permutations(s):
    print(''.join(i))