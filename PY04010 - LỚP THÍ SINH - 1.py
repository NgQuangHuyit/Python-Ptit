class ThiSinh:
    def __init__(self, name, birth, p1, p2, p3):
        self.name = name
        self.birth = birth
        self.score = p1 + p2 + p3

    def __str__(self):
        return f"{self.name} {self.birth} {self.score:.1f}"


name = input()
birth = input()
p1 = float(input())
p2 = float(input())
p3 = float(input())
a = ThiSinh(name, birth, p1, p2, p3)
print(a)
