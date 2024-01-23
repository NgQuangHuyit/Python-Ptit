class Employee:
    heso = {
        'A': {1: 10, 2: 10, 3: 10,
              4: 12, 5: 12, 6: 12, 7: 12, 8: 12,
              9: 14, 10: 14, 11: 14, 12: 14, 13: 14, 14: 14, 15: 14, 'more': 20},
        'B': {1: 10, 2: 10, 3: 10,
              4: 11, 5: 11, 6: 11, 7: 11, 8: 11,
              9: 13, 10: 13, 11: 13, 12: 13, 13: 13, 14: 13, 15: 13, 'more': 16},
        'C': {1: 9, 2: 9, 3: 9,
              4: 10, 5: 10, 6: 10, 7: 10, 8: 10,
              9: 12, 10: 12, 11: 12, 12: 12, 13: 12, 14: 12, 15: 12, 'more': 14},
        'D': {1: 8, 2: 8, 3: 8,
              4: 9, 5: 9, 6: 9, 7: 9, 8: 9,
              9: 11, 10: 11, 11: 11, 12: 11, 13: 11, 14: 11, 15: 11, 'more': 13}
    }

    def __init__(self, id, name, basSal, numberOfWorkdays):
        self.department = None
        self.id = id
        self.name = name
        self.basicSalary = int(basSal) * 1000
        self.numberOfWorkdays = int(numberOfWorkdays)
        self.totalSalary = 0

    def setDepartment(self, department):
        self.department = department

    def calSal(self):
        yearWork = int(self.id[1:3])
        if yearWork >= 16:
            yearWork = 'more'
        self.totalSalary = self.basicSalary * self.numberOfWorkdays * Employee.heso[self.id[0]][yearWork]

    def __str__(self):
        return f"{self.id} {self.name} {self.department} {self.totalSalary}"


department = {}
for i in range(int(input())):
    code, name = input().split(maxsplit=1)
    department[code] = name
empList = []
for i in range(int(input())):
    code = input()
    empList.append(Employee(code, input(), input(), input()))
    empList[i].setDepartment(department[code[-2:]])
    empList[i].calSal()
print(*empList, sep='\n')
"""
2
HC Hanh chinh
KH Ke hoach Dau tu
2
C06HC
Tran Binh Minh
65
25
D03KH
Le Hoa Binh
59
24
"""