num = []
for t in range(int(input())):
    s = list(input())
    for i in range(len(s)):
        if not s[i].isdigit():
            s[i] = ' '
    s = ''.join(s)
    num += list(map(int, s.split()))
num.sort()
print(*num, sep='\n')
