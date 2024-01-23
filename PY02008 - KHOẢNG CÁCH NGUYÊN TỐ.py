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


def genPrimes(n):
    yield 2
    cnt = 1
    num = 3
    while cnt < n:
        if isPrime(num):
            cnt += 1
            yield num
        num += 2


N, X = map(int, input().split())
res = [X]
for number in genPrimes(N):
    res.append(res[-1] + number)
print(*res)
