num = input()
i = 0
l = len(num)
num += '00'
ok = True
while i < l:
    if num[i:i+3] == '688':
        i += 3
    elif num[i:i+2] == '68':
        i += 2
    elif num[i] == '6':
        i += 1
    else:
        ok = False
        break
if ok:
    print('YES')
else:
    print('NO')