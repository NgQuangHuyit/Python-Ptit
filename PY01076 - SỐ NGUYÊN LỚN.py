def gcd(a, b):
    while a:
        b, a = a, b % a
    return b


for t in range(int(input())):
    a = int(input())
    b = int(input())
    print(gcd(a, b))
