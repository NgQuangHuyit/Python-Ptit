class Candidate:
    UT = {'1': 2.0, '2': 1.5, '3': 1.0, '4': 0.0}
    Subject = {'A': 'TOAN', 'B': 'LY', 'C': 'HOA'}
    ID = 1

    def __init__(self, name, code, tinHoc, chuyenMon):
        self.diem = 0
        self.name = name
        self.code = code
        self.tinHoc = tinHoc
        self.chuyenMon = chuyenMon
        self.ut = Candidate.UT[self.code[1]]
        self.sub = Candidate.Subject[self.code[0]]
        if Candidate.ID >= 10:
            self.id = 'GV' + str(Candidate.ID)
            Candidate.ID += 1
        else:
            self.id = 'GV0' + str(Candidate.ID)
            Candidate.ID += 1
        self.ketQua = None

    def xetTuyen(self):
        diem = self.tinHoc * 2 + self.chuyenMon + self.ut
        self.diem = diem
        if diem >= 18:
            self.ketQua = 'TRUNG TUYEN'
        else:
            self.ketQua = 'LOAI'

    def __str__(self):
        return f"{self.id} {self.name} {self.sub} {self.diem:.1f} {self.ketQua}"


ls = []
for t in range(int(input())):
    ls.append(Candidate(input(), input(), float(input()), float(input())))
    ls[t].xetTuyen()
ls.sort(key= lambda gv: -gv.diem)
print(*ls, sep='\n')
