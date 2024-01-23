N = int(input())
matrix = [0] * N
for i in range(N):
    matrix[i] = [int(num) for num in input().split()]
K = int(input())

upper = 0
bottom = 0
for i in range(0, N - 1):
    for j in range(N-i - 1):
        upper += matrix[i][j]

for i in range(1, N):
    for j in range(N - i, N):
        bottom += matrix[i][j]
dif = abs(bottom - upper)
if dif <= K:
    print('YES')
else:
    print('NO')
print(dif)
