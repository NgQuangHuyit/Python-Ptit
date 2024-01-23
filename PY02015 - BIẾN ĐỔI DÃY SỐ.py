while True:
    a, b, c, d = map(int, input().split())
    if [a, b, c, d] == [0, 0, 0, 0]:
        break
    cnt = 0
    while (a != b) or (a != c) or (a != d):
        cnt += 1
        tmp_a = a
        a = abs(a - b)
        b = abs(b - c)
        c = abs(c - d)
        d = abs(d - tmp_a)
    print(cnt)
