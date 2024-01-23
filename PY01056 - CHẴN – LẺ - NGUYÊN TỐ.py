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


for t in range(int(input())):
    N = list(map(int, list(input())))
    ok = True
    for i in range(0, len(N), 2):
        if N[i] % 2 != 0:
            ok = False
            break
    if ok:
        for i in range(1, len(N), 2):
            if N[i] % 2 == 0:
                ok = False
                break
    if ok:
        if not isPrime(sum(N)):
            ok = False
    if ok:
        print("YES")
    else:
        print("NO")
