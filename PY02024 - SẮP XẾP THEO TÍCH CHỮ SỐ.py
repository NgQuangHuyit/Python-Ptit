def sortBy(num:str):
    digits = [int(digit) for digit in num]
    mul = 1
    for digit in digits:
        if digit == 0:
            mul = 0
            break
        mul *= digit
    return tuple((mul, int(num)))


for t in range(int(input())):
    N = int(input())
    arr = [num for num in input().split()]
    arr.sort(key=sortBy)
    print(*arr)
