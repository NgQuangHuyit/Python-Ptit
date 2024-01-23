import cmath

class SoPhuc:
    def __init__(self, real1, imag1, real2, imag2):
        self.A = complex(real1, imag1)
        self.B = complex(real2, imag2)

    def cal1(self):
        number = (self.A + self.B) * self.A
        return number

    def cal2(self):
        number = (self.A + self.B) ** 2
        return number

    def __str__(self):
        res1 = self.cal1()
        res2 = self.cal2()
        if res1.imag < 0:
            res1 = f"{int(res1.real)} - {abs(int(res1.imag))}i"
        else:
            res1 = f"{int(res1.real)} + {int(res1.imag)}i"
        if res2.imag < 0:
            res2 = f"{int(res2.real)} - {abs(int(res2.imag))}i"
        else:
            res2 = f"{int(res2.real)} + {int(res2.imag)}i"
        return f"{res1}, {res2}"


for t in range(int(input())):
    arr = [int(i) for i in input().split()]
    soPhuc = SoPhuc(*arr)
    print(soPhuc)

