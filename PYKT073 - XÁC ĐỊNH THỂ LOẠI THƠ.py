poem = []
N = int(input())
for i in range(N):
    poem.append(input().split())
cnt = 0
kind = []
line = 0
while line < N:
    if len(poem[line]) == 7:
        kind.append(2)
        cnt += 1
        line += 4
    else:
        kind.append(1)
        cnt += 1
        while len(poem[line]) != 7:
            line += 1
            if line == N:
                break
print(cnt)
print(*kind, sep='\n')
