class Thisinh():
    def __init__(self, name, ngaysinh, diem1, diem2, diem3):
        self.name=name
        self.ngaysinh=ngaysinh
        self.diem1=diem1
        self.diem2=diem2
        self.diem3=diem3
    def out(self):
        print(self.name, self.ngaysinh, self.diem1+self.diem2+self.diem3)
if __name__=='__main__':
    thisinh=Thisinh(input(), input(), float(input()), float(input()), float(input()))
    thisinh.out()
