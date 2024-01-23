N = input()
step = 0
while len(N) > 1:
    step += 1
    sum = 0
    for digit in N:
        sum += ord(digit) - ord('0')
    N = str(sum)
print(step)
