for t in range(int(input())):
    N = int(input())
    arr = [num for num in input().split()]
    arr.sort(key=lambda x: (sum(list(map(int, list(x)))), int(x)))
    print(*arr)
