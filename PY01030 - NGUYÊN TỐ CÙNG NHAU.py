def check(a, b):
    while b:
        a, b = b, a % b
    if a == 1:
        return True
    else:
        return False


N, K =  map(int, input().split())
cnt = 0
for i in range(10 ** (K-1), 10 ** K):
    if check(N, i):
        print(i, end=' ')
        cnt += 1
        if cnt == 10:
            print('\n')
            cnt = 0
