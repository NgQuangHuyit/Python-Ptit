def check(num1, num2):
    while num1:
        num2, num1 = num1, num2 % num1
    if num2 == 1:
        return True
    return False


N = int(input())
arr = list(map(int, input().split()))
arr.sort()
for i in range(N-1):
    for j in range(i+1, N):
        if check(arr[i], arr[j]):
            print(f"{arr[i]} {arr[j]}")
