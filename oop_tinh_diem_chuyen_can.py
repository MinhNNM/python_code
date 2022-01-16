class Sinh_vien():
    def __init__(self, id, ten, lop):
        self.id=id
        self.ten=ten
        self.lop=lop
    def setdiem(self, s):
        m=s.count('m')
        v=s.count('v')
        n=10-m-2*v
        if n<=0:
            self.diem=0
        else:
            self.diem=n
    def DK(self):
        if self.diem==0:
            return "KDDK"
        else:
            return ""
    def tostring(self):
        return f'{self.id} {self.ten} {self.lop} {self.diem} {self.DK()}'
if __name__=='__main__':
    res=[]
    t=int(input())
    for i in range(t):
        id=input()
        name=input()
        lop=input()
        res.append(Sinh_vien(id, name, lop))
    for i in range(t):
        s=input().split(" ")
        for i in res:
            if i.id==s[0]:
                i.setdiem(s[1])
    for i in res:
        print(i.tostring())
