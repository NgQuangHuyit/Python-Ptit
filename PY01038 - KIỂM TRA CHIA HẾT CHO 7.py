for t in range(int(input())):
    N = int(input())
    ok = False
    for i in range(1000):
        if N % 7 == 0:
            print(N)
            ok = True
            break
        N += int(str(N)[::-1])
    if not ok:
        print(-1)
