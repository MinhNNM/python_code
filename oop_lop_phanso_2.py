def ucln(a, b):
    if b==0:
        return a
    return ucln(b, a%b)
class Phanso():
    def __init__(self, tu1, mau1, tu2, mau2):
        self.tu1=tu1
        self.mau1=mau1
        self.tu2=tu2
        self.mau2=mau2
    def rutgon(self):
        t1=int(self.tu1/ucln(self.tu1, self.mau1))
        m1=int(self.mau1/ucln(self.tu1, self.mau1))
        t2=int(self.tu2/ucln(self.tu2, self.mau2))
        m2=int(self.mau2/ucln(self.tu2, self.mau2))
        res1=t1*m2+t2*m1
        res2=m1*m2
        print(f'{int(res1/ucln(res1, res2))}/{int(res2/ucln(res1, res2))}')
if __name__=='__main__':
    arr=[int(i) for i in input().split()]
    ps1=Phanso(arr[0], arr[1], arr[2], arr[3])
    ps1.rutgon()