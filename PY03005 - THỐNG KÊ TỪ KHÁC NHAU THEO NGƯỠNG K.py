import re

n, k = map(int, input().split())
inputStream = ''
for i in range(n):
    inputStream = inputStream + ' ' + input().lower()
regex = r"[a-zA-Z0-9]+"
words = re.findall(regex, inputStream)
wordFreq = {}
for word in words:
    if word in wordFreq:
        wordFreq[word] += 1
    else:
        wordFreq[word] = 1
wordFreq = list(wordFreq.items())
wordFreq.sort(key=lambda a: (-a[1], a[0]))
for word in wordFreq:
    if word[1] >= k:
        print(f"{word[0]} {word[1]}")
'''PTIT duy tri hoc phi on dinh nam 2019 va khong tang trong nam 2020-2021 va 2021-2022!
Khi dich benh xuat hien PTIT trich hon 6 ty dong ho tro sinh vien PTIT
voi muc ho tro 500000 dong/sinh vien PTIT.'''
