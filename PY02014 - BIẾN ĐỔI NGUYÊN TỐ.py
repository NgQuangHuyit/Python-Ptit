isPrime = [1] * 100500
primes = []
isPrime[0] = isPrime[1] = 0
for i in range(2, 10500):
    if isPrime[i]:
        for j in range(i * i, 10500, i):
            isPrime[j] = 0
        primes.append(i)
n = int(input())
res = 0
for num in map(int, input().split()):
    minDistance = 100000
    for prime in primes:
        minDistance = min(minDistance, abs(num - prime))
    res = max(res, minDistance)
print(res)
