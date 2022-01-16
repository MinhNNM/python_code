class Sinhvien():
    def __init__(self, ten, C, T):
        self.ten=ten
        self.C=C
        self.T=T
    def tostring(self):
        return f'{self.ten} {self.C} {self.T}'
if __name__=='__main__':
    t=int(input())
    res=[]
    for i in range(t):
        s=input()
        a=[int(i) for i in input().split()]
        sv=Sinhvien(s, a[0], a[1])
        res.append(sv)
    res.sort(key=lambda x: (-x.C, x.T, x.ten))
    for i in res:
        print(i.tostring())
