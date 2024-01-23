vs = [False]
ke = {}

def dfs(u):
    global vs
    vs[u] = True
    for v in ke[u]:
        if not vs[v]:
            dfs(v)


N, M, X = map(int, input().split())
vs = [False] * (N + 1)
for i in range(1, N + 1):
    ke[i] = []
for i in range(M):
    u, v = map(int, input().split())
    ke[u].append(v)
    ke[v].append(u)
dfs(X)
for i in range(1, N+1):
    if not vs[i]:
        print(i)
