def check(s):
    check=1
    for i in s:
        if i!='_':
            check=0
    if check==1 and s.islapha():
        return True
    return False
s=input().lower()
if s[-3:]=='.py' and check(s):
    print("yes")
else:
    print('no')