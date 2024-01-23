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
    N = list(input())
    ok = True
    if not isPrime(len(N)):
        print("NO")
        continue
    cnt_prime_digit = 0
    for i in N:
        if isPrime(int(i)):
            cnt_prime_digit += 1
    if cnt_prime_digit > (len(N) - cnt_prime_digit):
        print("YES")
    else:
        print("NO")
