fibo = [0] * 94
fibo[0] = 0
fibo[1] = 1
for i in range(2, 94):
    fibo[i] = fibo[i-1] + fibo[i-2]

for t in range(int(input())):
    a, b = map(int, input().split())
    print(*fibo[a:b+1])
