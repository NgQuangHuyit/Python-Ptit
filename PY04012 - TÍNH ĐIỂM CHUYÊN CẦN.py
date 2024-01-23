class Student:
    def __init__(self, ma, hoTen, lop):
        self.ma = ma
        self.hoTen = hoTen
        self.lop = lop
        self.ketQua = 10

    def diemDanh(self, diemdanh):
        for buoi in diemdanh:
            if self.ketQua <= 0:
                break
            if buoi == 'v':
                self.ketQua -= 2
            elif buoi == 'm':
                self.ketQua -= 1
        if self.ketQua <= 0:
            self.ketQua = "0 KDDK"

    def __str__(self):
        return f"{self.ma} {self.hoTen} {self.lop} {self.ketQua}"


N = int(input())
studentList = {}
ls = []
for t in range(N):
    ma = input()
    ls.append(ma)
    studentList[ma] = Student(ma, input(), input())
for i in range(N):
    ma, diemdanh = input().split()
    studentList[ma].diemDanh(diemdanh)

for student in ls:
    print(studentList[student])
