n = int(input())
lines = []
res = []
i = 0
for j in range(n):
    s = input()
    if s == '':
        res.append(f'{lines[0]}: {len(lines) - 1}')
        lines.clear()
    else:
        lines.append(s)
        n -= 1
res.append(f'{lines[0]}: {len(lines) - 1}')
print(*res, sep='\n')
'''
9
Home/accommodation
What kind of housing/accommodation do you live in?
Who do you live with?
How long have you lived there?

Study
Describe your education
What is your area of specialization?
Why did you choose to study that major?
'''