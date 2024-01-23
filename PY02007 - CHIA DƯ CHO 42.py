a = []
while len(a) != 10:
    a.extend(list(map(int, input().split())))
res = [num % 42 for num in a]
res = set(res)
print(len(res))
