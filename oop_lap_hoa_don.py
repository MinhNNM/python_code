class Khach_hang():
    def __init__(self, id, ten, cscu, csmoi):
        self.id=id
        self.ten=ten
        self.cscu=cscu
        self.csmoi=csmoi
    def tongtien(self):
        x=self.csmoi-self.cscu
        if x<=50:
            s=x*100*1.02
        elif x<100:
            s=(50*100+(x-50)*150)*1.03
        else:
            s=(50*100+50*150+(x-100)*200)*1.05
        return int(round(s*10/10, 0))
    def tostring(self):
        return f'{self.id} {self.ten} {self.tongtien()}'
if __name__=='__main__':
    t=int(input())
    res=[]
    for i in range(1, t+1):
        s=input()
        cscu=int(input())
        csmoi=int(input())
        if i<10:
            id="KH0"+str(i)
        else:
            id="KH"+str(i)
        res.append(Khach_hang(id, s, cscu, csmoi))
    res.sort(key=lambda x: (-x.tongtien()))
    for i in res:
        print(i.tostring())
