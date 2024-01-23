for t in range(int(input())):
    N = int(input())
    cnt = 0
    for i in range(2, 40000):
        if (2 * N) % i == 0:
            hieu = i - 1
            tong = 2*N / i
            cuoi = int((tong + hieu)/2)
            dau = int((tong - hieu)/2)
            if dau + cuoi == tong and cuoi - dau == hieu and dau > 0:
                cnt += 1
    print(cnt)