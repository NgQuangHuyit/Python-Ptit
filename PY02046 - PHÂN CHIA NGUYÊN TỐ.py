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


N = int(input())
arrA = list(map(int, input().split()))
arrB = []
for num in arrA:
    if num not in arrB:
        arrB.append(num)
ok = False
for i in range(len(arrB)):
    if isPrime(sum(arrB[0:i+1])):
        if isPrime(sum(arrB[i+1:])):
            print(i)
            ok = True
            break
if not ok:
    print('NOT FOUND')
