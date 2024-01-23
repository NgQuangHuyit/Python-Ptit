class Subject:
    def __init__(self, code, name, method):
        self.code = code
        self.name = name
        self.method = method

    def __str__(self):
        return f"{self.code} {self.name} {self.method}"


subjList = []
for t in range(int(input())):
    subjList.append(Subject(input(), input(), input()))
subjList.sort(key=lambda sub: sub.code)
print(*subjList, sep='\n')
