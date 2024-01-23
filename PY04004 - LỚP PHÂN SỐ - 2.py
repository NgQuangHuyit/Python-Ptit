class PhanSo:
    def __init__(self, tuso, mauso):
        self.tu = tuso
        self.mau = mauso
        self.toigian()

    def toigian(self):
        tuso = self.tu
        mauso = self.mau
        while tuso:
            mauso, tuso = tuso, mauso % tuso
        self.tu /= mauso
        self.mau /= mauso

    def display(self):
        print(f"{int(self.tu)}/{int(self.mau)}")


    def congPhanSo(self, ps2):
        mauSo1 = self.mau
        mauSo2 = ps2.mau
        while mauSo2:
            mauSo1, mauSo2 = mauSo2, mauSo1%mauSo2
        lcm = self.mau * ps2.mau // mauSo1
        tuSo = self.tu * (lcm / self.mau) + ps2.tu * (lcm / ps2.mau)
        mauSo = lcm
        return PhanSo(tuSo, mauSo)


tu1, mau1, tu2, mau2 = map(int, input().split())
p1 = PhanSo(tu1, mau1)
p2 = PhanSo(tu2, mau2)
p3 = p1.congPhanSo(p2)
p3.display()
