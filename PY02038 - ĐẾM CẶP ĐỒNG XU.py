N = int(input())
matrix = []
rowCnt = [0] * N
colCnt = [0] * N
for i in range(N):
    matrix.append(list(input()))
    for j in range(N):
        if matrix[i][j] == 'C':
            rowCnt[i] += 1
            colCnt[j] += 1
res = 0
for r in rowCnt:
    C_2_r = r * (r - 1) / 2
    res += C_2_r
for c in colCnt:
    C_2_c = c * (c - 1) / 2
    res += C_2_c
print(int(res))
