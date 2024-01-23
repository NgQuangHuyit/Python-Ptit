class KH:
    ID = 1

    def __init__(self, ten, cu, moi):
        self.ten = ten
        self.cu = cu
        self.moi = moi
        self.cnt = moi - cu
        self.tongphi = 0
        self.id = "KH{:0>2}".format(KH.ID)
        KH.ID += 1

    def tinhTien(self):
        if self.cnt <= 50:
            m1 = self.cnt
            m2 = 0
            m3 = 0
            rate = 1.02
        elif self.cnt <= 100:
            m1 = 50
            m2 = self.cnt - m1
            m3 = 0
            rate = 1.03
        else:
            m1 = 50
            m2 = 50
            m3 = self.cnt - m1 - m2
            rate = 1.05
        self.tongphi = (m1 * 100 + m2 * 150 + m3 * 200) * rate

    def __str__(self):
        return f"{self.id} {self.ten} {self.tongphi:.0f}"

ds = []
for _ in range(int(input())):
    kh = KH(input(), int(input()), int(input()))
    kh.tinhTien()
    ds.append(kh)
ds.sort(key=lambda k: -k.tongphi)
print(*ds,sep='\n')

'''
3
Le Thi Thanh
468
500
Le Duc Cong
160
230
Ha Hue Anh
410
612
'''


