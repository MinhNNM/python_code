from datetime import datetime
class Hoa_don():
    def __init__(self, id, ten, sophong, ngayv, ngayr, dv):
        self.id=id
        self.ten=ten
        self.sophong=sophong
        self.ngayv=ngayv
        self.ngayr=ngayr
        self.dv=dv
    def dongia(self):
        s=str(self.sophong)
        x=int(s[0])
        if x==1:
            return 25
        elif x==2:
            return 34
        elif x==3:
            return 50
        return 80
    def so_ngay(self):
        tmp='%d/%m/%Y'
        vao=datetime.strptime(self.ngayv, tmp)
        ra=datetime.strptime(self.ngayr, tmp)
        return (ra-vao).days+1
    def tien(self):
        return self.so_ngay()*self.dongia()+self.dv
    def tostring(self):
        print(f'{self.id} {self.ten} {self.sophong} {self.so_ngay()} {self.tien()}')
if __name__=='__main__':
    t=int(input())
    res=[]
    for i in range(1, t+1):
        if i<10:
            id="KH0"+str(i)
        else:
            id="KH"+str(i)
        ten=input().strip()
        sophong=int(input())
        ngayv=input().strip()
        ngayr=input().strip()
        dv=int(input())
        tm=Hoa_don(id, ten, sophong, ngayv, ngayr, dv)
        res.append(tm)        
    res.sort(key=lambda x: (-x.tien()))
    for i in res:
        i.tostring()


# input:
# 3
# Huynh Van Thanh   
# 103 
# 05/06/2010   
# 05/06/2010   
# 15
# Le Duc Cong  
# 106 
# 08/03/2010   
# 01/05/2010   
# 220
# Tran Thi Bich Tuyen   
# 207 
# 10/04/2010   
# 21/04/2010   
# 96

# ouput:
# KH02 Le Duc Cong 106 55 1595
# KH03 Tran Thi Bich Tuyen 207 12 504
# KH01 Huynh Van Thanh 103 1 40