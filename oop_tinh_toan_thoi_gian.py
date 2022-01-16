from datetime import datetime
class Thoigian():
    def __init__(self, id, ten, vao, ra):
        self.id=id
        self.ten=ten
        self.vao=vao
        self.ra=ra
    def thoi_gian(self):
        tmp='%H:%M'
        x=str(datetime.strptime(self.ra, tmp)-datetime.strptime(self.vao, tmp))
        st=x.split(':')
        return st
    def tgian(self):
        sum=self.thoi_gian()[0]+self.thoi_gian()[1]
        return int(sum)
    def tostring(self):
        x=int(self.thoi_gian()[1])
        s=str(x)
        return f'{self.id} {self.ten} {self.thoi_gian()[0]} gio {s} phut'
if __name__=='__main__':
    t=int(input())
    res=[]
    for i in range(t):
        id=input()
        name=input()
        time_vao=input()
        time_ra=input()
        tg=Thoigian(id, name, time_vao, time_ra)
        res.append(tg)
    res.sort(key=lambda x: (-x.tgian()))
    for i in res:
        print(i.tostring())
