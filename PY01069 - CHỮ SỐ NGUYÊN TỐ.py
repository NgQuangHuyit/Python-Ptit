def check(s):
    if s[-1] == '2':
        return False
    check = [0] * 4
    for i in s:
        for j in range(4):
            if i == primeDigits[j]:
                check[j] = 1
    if sum(check) == 4:
        return True
    return False


def Try(k, s):
    if k >= 4:
        if check(s):
            res.append(s)
    if k == n:
        return
    for i in range(4):
        Try(k + 1, s + primeDigits[i])


primeDigits = ['2', '3', '5', '7']
res = []
n = int(input())
Try(0, '')
res = sorted(res, key=lambda x: len(x))
print(*res, sep='\n')
