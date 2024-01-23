from math import sqrt


def isPrime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True


def check(number, limit):
    if number == number[-1::-1] or int(number[-1::-1]) > limit:
        return False
    if not isPrime(int(number)):
        return False
    if not isPrime(int(number[-1::-1])):
        return False
    return True


for t in range(int(input())):
    N = int(input())
    res = []
    for i in range(13, N, 2):
        num = str(i)
        if check(num, N) and num not in res:
            res.append(num)
            res.append(num[-1::-1])
    print(*res)

