N, M = map(int, input().split())
matrix = [0] * N
for i in range(N):
    matrix[i] = input().split()
if N > M:
    cnt = N - M
    for i in range(cnt):
        del matrix[i]
elif M > N:
    cnt = M - N
    for i in range(N):
        for j in range(1, cnt+1):
            del matrix[i][j]
row = len(matrix)
for i in range(row):
    print(*matrix[i])
'''
6 4
2 8 7 6
6 3 2 6
7 2 2 8
9 9 9 8
9 6 6 3
7 7 4 9

4 6
2 8 7 6 4 3
6 3 2 6 7 2
7 2 2 8 9 1
9 9 9 8 0 7

'''