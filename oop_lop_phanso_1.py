def ucln(a, b):
    if b==0:
        return a
    return ucln(b, a%b)
class Phanso():
    def __init__(self, tu, mau):
        self.tu=tu
        self.mau=mau
    def rutgon(self):
        r1=int(self.tu/ucln(self.tu, self.mau))
        r2=int(self.mau/ucln(self.tu, self.mau))
        print(f'{r1}/{r2}')
if __name__=='__main__':
    arr=[int(i) for i in input().split()]
    ps1=Phanso(arr[0], arr[1])
    ps1.rutgon()