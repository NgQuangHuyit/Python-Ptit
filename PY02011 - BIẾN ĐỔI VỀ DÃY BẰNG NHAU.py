n = int(input())
arr = list(map(int, input().split()))
minStep = 999999999
val = arr[0]
for num in arr:
    stepCnt = 0
    for j in arr:
        stepCnt += abs(num - j)
    if minStep > stepCnt:
        minStep = stepCnt
        val = num
print(minStep, val)
'''
8
13 5 8 7 9 15 26 34
'''