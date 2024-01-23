class HoGiaDinnh:
    cnt = 1

    dinhmuc = {
        'A': 100,
        'B': 500,
        'C': 200
    }


    def __init__(self, name: str, loai, count):
        self.name = " ".join([s.capitalize() for s in name.strip().lower().split()])
        self.type = loai
        self.ma = "KH{:0>2}".format(HoGiaDinnh.cnt)
        HoGiaDinnh.cnt += 1
        self.dinhmuc = HoGiaDinnh.dinhmuc[loai.upper()]
        self.count = count


    def trongdinhmuc(self):
        if self.count <= self.dinhmuc:
            return self.count * 450
        else:
            return self.dinhmuc * 450

    def vuotdinhmuc(self):
        if self.count <= self.dinhmuc:
            return 0
        else:
            return (self.count - self.dinhmuc) * 1000

    def vat(self):
        return self.vuotdinhmuc() // 20

    def total(self):
        return self.trongdinhmuc() + self.vuotdinhmuc() + self.vat()

    def __str__(self):
        return f"{self.ma} {self.name} {self.trongdinhmuc()} {self.vuotdinhmuc()} {self.vat()} {self.total()}"

list = []

for i in range(int(input())):
    name = input()
    loai, dau, cuoi = input().strip().split()
    list.append(HoGiaDinnh(name=name,loai=loai, count= int(cuoi) - int(dau)))

list.sort(key= lambda a: -a.total())
print(*list, sep='\n')

