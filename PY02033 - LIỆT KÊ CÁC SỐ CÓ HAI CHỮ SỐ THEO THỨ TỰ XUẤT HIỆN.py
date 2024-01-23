N = input()
res = []
for i in range(0, len(N)-1, 2):
    num = N[i] + N[i + 1]
    if num not in res:
        res.append(num)
print(*res)

