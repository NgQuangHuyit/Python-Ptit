MAX = int(1e6+1)

primes = [1]*int(MAX)
primes[0] = primes[1] = 0
for i in range(1000):
    if primes[i]:
        for j in range(i*i, MAX, i):
            primes[j] = 0

for t in range(int(input())):
    cnt = 0
    for i in range(int(input())-5):
        if primes[i] and primes[i+6]:
            if primes[i+2] or primes[i+4]:
                cnt += 1
    print(cnt)
