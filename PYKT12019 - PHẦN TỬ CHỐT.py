for t in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    left = [0] * (n+1)
    left[0] = 0
    left[1] = arr[0]
    for i in range(1, n + 1):
        left[i] = max(left[i-1], arr[i-1])
    right = [0] * n
    right[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        right[i] = min(right[i+1], arr[i])
    right.append(1000000001)
    cnt = 0
    for i in range(0, n):
       if left[i] <= arr[i] < right[i+1]:
            cnt += 1
    print(cnt)

