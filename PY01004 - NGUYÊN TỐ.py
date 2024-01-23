import math


def check(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    if a > 1:
        return False
    return True


def is_prime_num(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    sqrt_num = int(math.sqrt(number))
    for i in range(5, sqrt_num + 1, 6):
        if number % i == 0 or number % (i + 2) == 0:
            return False
    return True


for _i in range(int(input())):
    N = int(input())
    K = 1
    for i in range(2, N):
        if check(N, i):
            K += 1
    if is_prime_num(K):
        print("YES")
    else:
        print('NO')
