class DS():
    def __init__(self, ma, ten, ht):
        self.ma=ma
        self.ten=ten
        self.ht=ht
    def tostring(self):
        return f'{self.ma} {self.ten} {self.ht}'
if __name__=='__main__':
    t=int(input())
    res=[]
    for i in range(t):
        ma=input()
        ten=input()
        ht=input()
        res.append(DS(ma, ten, ht))
    res.sort(key=lambda x:(x.ma))
    for i in res:
        print(i.tostring())
