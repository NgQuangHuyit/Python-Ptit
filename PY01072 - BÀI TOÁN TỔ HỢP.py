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
numSet = list(set(map(int, input().split())))
numSet.sort()
N = len(numSet)
for index_arr in gen(N, K):
    if index_arr != -1:
        combine = []
        for index in index_arr:
            combine.append(numSet[index - 1])
        print(*combine)
    else:
        break
