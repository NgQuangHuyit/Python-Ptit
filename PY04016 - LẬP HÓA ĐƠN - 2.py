from datetime import  datetime as dt


class KhachHang:
    ID = 1

    def __init__(self, ten, soPhong, checkin, checkout, phiDvu):
        self.ten = ten
        self.soPhong = soPhong
        self.tang = soPhong[0]
        self.checkin = dt.strptime(checkin.strip(), "%d/%m/%Y")
        self.checkout = dt.strptime(checkout.strip(), "%d/%m/%Y")
        self.soNgay = self.checkout - self.checkin
        self.phiDvu = phiDvu
        self.thanhTien = 0
        self.id = f"KH{KhachHang.ID:0>2}"
        KhachHang.ID += 1

    def tinhTien(self):
        if self.tang == "1":
            self.thanhTien = (self.soNgay.days + 1) * 25 + self.phiDvu
        if self.tang == "2":
            self.thanhTien = (self.soNgay.days + 1) * 34 + self.phiDvu
        if self.tang == "3":
            self.thanhTien = (self.soNgay.days + 1) * 50 + self.phiDvu
        if self.tang == "4":
            self.thanhTien = (self.soNgay.days + 1) * 80 + self.phiDvu

    def __str__(self):
        return f"{self.id} {self.ten} {self.soPhong} {int(self.soNgay.days + 1)} {self.thanhTien}"


ds = []
for _ in range(int(input())):
    kh = KhachHang(input(), input(), input(), input(), int(input()))
    kh.tinhTien()
    ds.append(kh)

ds.sort(key=lambda k:-k.thanhTien)
print(*ds, sep='\n')
'''
3
Huynh Van Thanh   
103 
05/06/2010   
05/06/2010   
15
Le Duc Cong  
106 
08/03/2010   
01/05/2010   
220
Tran Thi Bich Tuyen   
207 
10/04/2010   
21/04/2010   
96
'''