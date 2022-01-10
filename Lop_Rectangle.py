class Rectangle():
    def __init__(self, dai, rong, color):
        self.dai=dai
        self.rong=rong
        self.color=color
    def out(self):
        if self.dai<=0 or self.rong<=0:
            print("INVALID")
        else:
            p=(self.dai+self.rong)*2
            res=self.dai*self.rong
            x=self.color
            x=x.lower().capitalize()
            print(p, res, x)
if __name__ =='__main__':
    arr=input().split()
    hcn=Rectangle(int(arr[0]), int(arr[1]), arr[2])
    hcn.out()