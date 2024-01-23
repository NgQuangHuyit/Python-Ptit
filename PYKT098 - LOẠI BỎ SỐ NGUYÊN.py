def isInteger(s):
    num = 0
    for c in s:
        if not c.isdigit():
            return True
        num = num * 10 + int(c)
    if 2147483647 >= num >= -2147483648:
        return False
    return True


file = open('DATA.in', 'r')
a = []
for line in file:
    for i in line.split():
        if isInteger(i):
            a.append(i)
for i in sorted(a):
    print(i, end=' ')
