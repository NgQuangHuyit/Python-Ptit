n, m = map(int, input().split())
matrix = []
maxVal = 0
minVal = 10000
for i in range(n):
    matrix.append([int(i) for i in input().split()])
    maxVal = max(max(matrix[i]), maxVal)
    minVal = min(min(matrix[i]), minVal)
luckyNum = maxVal - minVal
ok = False
locate = []
for i in range(n):
    for j in range(m):
        if matrix[i][j] == luckyNum:
            locate.append(f'Vi tri [{i}][{j}]')
            ok = True
if not ok:
    print('NOT FOUND')
else:
    print(luckyNum)
    print(*locate, sep='\n')
