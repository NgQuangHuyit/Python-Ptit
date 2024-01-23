for t in range(int(input())):
    S = input()
    N = input()
    cnt = 0
    i = 0
    l = len(N)
    while True:
        i = S.find(N, i)
        if i == -1:
            break
        cnt += 1
        i += l
    print(cnt)