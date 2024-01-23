for t in range(int(input())):
    n = int(input())
    arr = set(map(int, input().split()))
    L = min(arr)
    R = max(arr)
    dist = R - L + 1
    print(dist - len(arr))
