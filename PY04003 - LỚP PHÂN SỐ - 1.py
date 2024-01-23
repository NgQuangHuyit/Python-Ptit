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


tuso, mauso = map(int, input().split())
p = PhanSo(tuso, mauso)
p.display()
