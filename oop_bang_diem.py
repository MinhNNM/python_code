class Bangdiem():
    def __init__(self, id, ten, diem_a):
        self.id=id
        self.ten=ten
        self.diem_a=diem_a
    def diemtb(self):
        diem=(self.diem_a[0]+self.diem_a[1])*2
        for i in range(2, 10):
            diem+=self.diem_a[i]
        return round(diem/12+0.01, 1)
    def XL(self):
        if self.diemtb()>=9:
            return "XUAT SAC"
        elif self.diemtb()>=8 and self.diemtb()<9:
            return "GIOI"
        elif self.diemtb()>=7 and self.diemtb()<8:
            return "KHA"
        elif self.diemtb()>=5 and self.diemtb()<7:
            return "TB"
        return "YEU"
    def tostring(self):
        return f"{self.id} {self.ten} {self.diemtb()} {self.XL()}"
if __name__=='__main__':
    t=int(input())
    res=[]
    for i in range(1, t+1):
        if i<10:
            id="HS0"+str(i)
        else:
            id="HS"+str(i)
        name=input()
        a=[float(k) for k in input().split()]
        res.append(Bangdiem(id, name, a))
    res.sort(key=lambda x: (-x.diemtb(), x.id))
    for i in res:
        print(i.tostring())