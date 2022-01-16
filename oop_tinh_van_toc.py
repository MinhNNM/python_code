from datetime import datetime


class Vantoc():
    def __init__(self, ten, dc, tg):
        self.ten=ten
        self.dc=dc
        self.tg=tg
    def Ma(self):
        st=""
        dc=self.dc.split(' ')
        ten=self.ten.split(' ')
        for i in range(len(dc)):
            st+=dc[i][0]
        for i in range(len(ten)):
            st+=ten[i][0]
        return st
    def vantoc(self):
        x=self.tg.split(':')
        gio=int(x[0])-6
        phut=int(x[1])/60
        vt=120/(gio+phut)
        return vt
    def tostring(self):
        return f'{self.Ma()} {self.ten} {self.dc} {int(round(self.vantoc()*10/10,0))} Km/h'
if __name__=='__main__':
    t=int(input())
    res=[]
    for i in range(t):
        ten=input()
        dc=input()
        tg=input()
        res.append(Vantoc(ten, dc, tg))
    res.sort(key=lambda x: (-x.vantoc()))
    for i in res:
        print(i.tostring())
