def gen(n, k):
    arr = []
    for i in range(1, k + 1):
        arr.append(i)
    yield arr
    stop = False
    while not stop:
        i = k - 1
        while arr[i] == (n - k + i + 1):
            i -= 1
        if i < 0:
            stop = True
        else:
            arr[i] += 1
            for j in range(i+1, k):
                arr[j] = arr[j-1] + 1
            yield arr
    yield -1


N, K = map(int, input().split())
names = set(input().split())
names = list(names)
names.sort()
N = len(names)
for idArr in gen(N, K):
    if idArr == -1:
        break
    res = [names[idArr[i] - 1] for i in range(K)]
    print(*res)
