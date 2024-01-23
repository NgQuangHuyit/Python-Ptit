res = []
for t in range(int(input())):
    name = input()
    C, T = map(int, input().split())
    res.append((name, C, T))
res.sort(key=lambda x: (-x[1], x[2], x[0]))
for student in res:
    print(f"{student[0]} {student[1]} {student[2]}")
