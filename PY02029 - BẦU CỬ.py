N, M = map(int, input().split())
uv = {}
for vote in map(int, input().split()):
    uv[vote] = uv.setdefault(vote, 0) + 1
maxVote = max(list(uv.values()))
keys = list(uv.keys())
keys.sort()
winnerVote = 0
winner = -1
for key in keys:
    if uv[key] != maxVote and uv[key] > winnerVote:
        winnerVote = uv[key]
        winner = key

if winner == -1:
    print('NONE')
else:
    print(winner)
'''
10 4
2 3 1 2 3 4 1 2 3 2

8 5
1 2 3 4 4 3 2 1
8 4
1 2 3 4 4 3 2 1
'''
