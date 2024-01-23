while True:
    N = int(input())
    if N == 0:
        break
    arr = []
    for i in range(N):
        arr.append(int(input()))
    maxVal = max(arr)
    minVal = min(arr)
    if maxVal == minVal:
        print('BANG NHAU')
    else:
        print(minVal, maxVal, sep=' ')
