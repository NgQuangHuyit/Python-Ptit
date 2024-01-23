N = int(input())
B = [0] * (N + 1)
for i in range(1, N+1):
    B[i] = [None] + list(map(int, input().split()))
A = {}
if N == 2:
    A[1] = A[2] = B[2][1]/2
else:
    for i in range(2, N):
        A[i] = (B[i+1][i] - B[i+1][i-1] + B[i][i-1])/2
    A[1] = B[1][2] - A[2]
    A[N] = B[N][N-1] - A[N-1]
index = list(A.keys())
index.sort()
res = []
for i in index:
    res.append(int(A[i]))
print(*res)

"""
4
0 3 6 7
3 0 5 6
6 5 0 9
7 6 9 0

2
0 2
2 0
"""