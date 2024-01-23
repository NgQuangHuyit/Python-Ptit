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

prime_digits = [2, 3, 5, 7]

for t in range(int(input())):
    N = list(map(int, list(input())))
    ok = True
    for i in range(len(N)):
        if isPrime(i):
            if N[i] not in prime_digits:
                ok = False
                break
        else:
            if N[i] in prime_digits:
                ok = False
                break
    if ok:
        print("YES")
    else:
        print("NO")
