class Student:
    ID = 1

    def __init__(self, name, opp, cpp, thcs2):
        self.rank = 0
        self.total = opp * 3 + cpp * 3 + thcs2 * 2
        self.avg = '{:.2f}'.format(self.total/8 + 0.001)
        self.name = name
        if Student.ID < 10:
            self.id = 'SV0' + str(Student.ID)
            Student.ID += 1
        else:
            self.id = 'SV' + str(Student.ID)
            Student.ID += 1

    def setRank(self, rank):
        self.rank = rank

    def __str__(self):
        return f"{self.id} {self.name} {self.avg} {self.rank}"


studentList = []
for t in range(int(input())):
    name = [n.capitalize() for n in input().split()]
    name = ' '.join(name)
    studentList.append(Student(name, float(input()), float(input()), float(input())))
studentList.sort(key=lambda st: (-float(st.avg), st.id))
rk = 1
studentList[0].setRank(1)
for i in range(1, len(studentList)):
    if studentList[i].avg == studentList[i - 1].avg:
        studentList[i].setRank(studentList[i-1].rank)
        rk += 1
    else:
        rk += 1
        studentList[i].setRank(rk)
print(*studentList, sep='\n')
'''
2
 ha Thi kieu     anh
7
6
7
Pham    THI  HAO
6
7
6
'''