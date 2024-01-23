for t in range(int(input())):
    N, d = map(int, input().split())
    arr = list(map(int, input().split()))
    d = d % N
    for i in range(d):
        arr.append(arr[i])
    for i in range(d):
        del arr[0]
    print(*arr)
