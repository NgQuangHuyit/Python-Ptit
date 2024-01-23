s = input()
k = int(input())
freq = {}
for i in range(0, len(s), 2):
    if i == len(s) - 1:
        break
    num = s[i] + s[i+1]
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
res = []
for key in freq:
    if freq[key] >= k:
        res.append((int(key), freq[key]))
res.sort(key=lambda num: num[0])
if res:
    for num in res:
        print(f'{num[0]} {num[1]}')
else:
    print('NOT FOUND')
