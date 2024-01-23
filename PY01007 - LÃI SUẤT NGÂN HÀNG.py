from math import log, ceil

for i in range(int(input())):
    N, X, M = list(map(float, input().split()))
    n = log(M/N, (1+X/100))
    print(ceil(n))
