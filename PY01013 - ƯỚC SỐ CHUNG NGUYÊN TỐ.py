from math import sqrt

def gcd(num1, num2):
    while num1 != num2:
        if num1 > num2:
            num1 -= num2
        else:
            num2 -= num1
    return num1


def is_prime(num):
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


def sum_of_digits(num:int) -> int:
    digits = list(str(num))
    return sum(map(int, digits))

if __name__ == '__main__':
    for i in range(int(input())):
        a, b = map(int, input().split())
        GCD = gcd(a, b)
        if is_prime(sum_of_digits(GCD)):
            print("YES")
        else:
            print("NO")
