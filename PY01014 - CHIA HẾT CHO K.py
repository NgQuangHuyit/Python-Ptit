a, K, N = map(int, input().split())
i = 1
ok = False
while K * i <= N:
    b = K * i - a
    if b > 0:
        print(b, end=' ')
        ok = True
    i += 1
if not ok:
    print(-1)
