def check(s):
    if s[0]=='8':
        return False
    elif '888' in s:
        return False
    for i in s:
        if i!='6' and i!='8':
            return False
    return True
s=input()
if check(s):
    print("YES")
else:
    print("NO")