for t in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    numFreq = {}
    for num in arr:
        numFreq[num] = numFreq.setdefault(num, 0) + 1
    for key in numFreq.keys():
        if numFreq[key] % 2 != 0:
            print(key)
            break
