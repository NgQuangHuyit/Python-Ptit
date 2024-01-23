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


s = input()
for res in sinhHoanVi(len(s)):
    if res == -1:
        break
    xau = ""
    for i in range(len(s)):
        xau += s[res[i] - 1]
    print(xau)
