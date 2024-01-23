while True:
    N = int(input())
    if N == 0:
        break
    res = set()
    while N != 1:
        if N % 2 == 0:
            res.add(N/2)
            N /= 2
        else:
            res.add(N*3 + 1)
            N = N * 3 + 1
    print(len(res) + 1)
