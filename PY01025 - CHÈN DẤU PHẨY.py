N = list(input())
N.reverse()
l = len(N) + int((len(N) - 1)/3)
for i in range(3, l, 4):
    N.insert(i, ',')
N.reverse()
print(''.join(N))
