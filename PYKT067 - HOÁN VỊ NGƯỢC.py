def sinhHoanVi(n: int) -> list:
    res = []
    for i in range(n):
        res.append(i + 1)
    yield res

    while True:
        i = n - 2
        while res[i] > res[i + 1]:
            i -= 1
        if i == -1:
            return -1
        l = n - 1
        while res[l] < res[i]:
            l -= 1
        tmp = res[i]
        res[i] = res[l]
        res[l] = tmp
        head = res[:i + 1]
        tail = res[i + 1:]
        tail.sort()
        res = head + tail
        yield res


for t in range(int(input())):
    N = int(input())
    res = []
    for i in sinhHoanVi(N):
        i = list(map(str, i))
        res.append(''.join(i))
    res.reverse()
    print(len(res))
    print(*res, sep=' ')