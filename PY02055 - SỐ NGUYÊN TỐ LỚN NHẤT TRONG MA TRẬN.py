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


n, m = map(int, input().split())
matrix = []
prime = -1

for i in range(n):
    matrix.append([int(i) for i in input().split()])
    for j in matrix[i]:
        if isPrime(j) and j > prime:
            prime = j

if prime == -1:
    print('NOT FOUND')
else:
    print(prime)
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == prime:
                print(f'Vi tri [{i}][{j}]')
