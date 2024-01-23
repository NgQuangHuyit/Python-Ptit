N = int(input())
scores = list(map(float, input().split()))
scores.sort()
max_score = scores[-1]
min_score = scores[0]
valid_scores = []
for i in range(len(scores)):
    if scores[i] != max_score and scores[i] != min_score:
        valid_scores.append(scores[i])
final_score = sum(valid_scores) / len(valid_scores)
print('{:.2f}'.format(final_score))
