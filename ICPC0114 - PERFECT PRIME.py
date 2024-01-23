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


def check(number):
    if not isPrime(int(number)):
        return False
    if not isPrime(int(number[-1::-1])):
        return False
    sumDigits = 0
    for digit in number:
        if not isPrime(int(digit)):
            return False
        sumDigits += int(digit)
    if not isPrime(sumDigits):
        return False
    return True


for t in range(int(input())):
    N = input()
    if check(N):
        print('Yes')
    else:
        print('No')
