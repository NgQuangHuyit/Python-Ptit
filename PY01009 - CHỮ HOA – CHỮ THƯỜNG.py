s = input()
cnt_upper = cnt_lower = 0
for c in s:
    if c.islower():
        cnt_lower += 1
    else:
        cnt_upper += 1
if cnt_lower >= cnt_upper:
    print(s.lower())
else:
    print(s.upper())
