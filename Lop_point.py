from math import sqrt
class Point():
    def __init__(self, x1, y1, x2, y2):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
    def out(self):
        x=abs(self.x2-self.x1)
        y=abs(self.y1-self.y2)
        res=sqrt(x**2+y**2)
        return str("{:.4f}".format(res))
if __name__=='__main__':
    t=int(input())
    while t>0:
        arr=[float(i) for i in input().split()]
        point=Point(arr[0], arr[1], arr[2], arr[3])
        print(point.out())
        t-=1