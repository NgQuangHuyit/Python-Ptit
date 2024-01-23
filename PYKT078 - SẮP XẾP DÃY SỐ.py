for t in range(int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    maxVal = max(arr)
    dic = {}
    for i in range(len(arr)):
        if arr[i] == maxVal:
            arr.insert(i, m)
            break
    positive = []
    negative = []
    for num in arr:
        if num >= 0:
            positive.append(num)
        else:
            negative.append(num)
    print(*(negative + positive), sep=' ')