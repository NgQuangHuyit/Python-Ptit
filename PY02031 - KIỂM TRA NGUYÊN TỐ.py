N, M = map(int, input().split())
matrix = []
max_num = 0
for i in range(N):
    matrix.append([num for num in map(int, input().split())])
    if max_num < max(matrix[i]):
        max_num = max(matrix[i])
# Sang nguyen to
is_prime = [True] * (max_num + 1)
is_prime[1] = False
for i in range(1, max_num + 1):
    if is_prime[i]:
        for j in range(i * i, max_num +1, i):
            is_prime[j] = False

for i in range(N):
    for j in range(M):
        if is_prime[matrix[i][j]]:
            matrix[i][j] = 1
        else:
            matrix[i][j] = 0

for i in range(N):
    print(*matrix[i])

