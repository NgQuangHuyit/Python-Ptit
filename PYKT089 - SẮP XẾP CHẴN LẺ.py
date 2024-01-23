try:
    N = int(input())
    oddNum = []
    oddIndex = []
    evenNum = []
    evenIndex = []
    arr = []
    while True:
        x = list(map(int, input().split()))
        arr += x
        if len(arr) == N:
            break
    for i in range(N):
        if arr[i] % 2 == 0:
            evenNum.append(arr[i])
            evenIndex.append(i)
        else:
            oddNum.append(arr[i])
            oddIndex.append(i)
    evenNum.sort()
    oddNum.sort(reverse=True)
    even = 0
    for index in evenIndex:
        arr[index] = evenNum[even]
        even += 1
    odd = 0
    for index in oddIndex:
        arr[index] = oddNum[odd]
        odd += 1
    print(*arr)

except:
    pass
