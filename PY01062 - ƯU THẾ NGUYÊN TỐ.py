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
    N = list(map(int, input()))
    ok = True
    if not isPrime(len(N)):
        ok = False
    if ok:
        cnt_prime_digit = 0
        for i in N:
            if i in prime_digits:
                cnt_prime_digit += 1
        if cnt_prime_digit <= (len(N) - cnt_prime_digit):
            ok = False
    if ok:
        print("YES")
    else:
        print("NO")
