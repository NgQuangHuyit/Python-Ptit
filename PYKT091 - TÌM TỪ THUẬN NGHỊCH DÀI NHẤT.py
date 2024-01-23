with open('VANBAN.in', mode='r') as f:
    data = f.read()
data = data.split()
dic = {}
lenMax = 0
for word in data:
    if word != word[::-1]:
        continue
    if word in dic:
        dic[word] += 1
    else:
        if len(word) > lenMax:
            lenMax = len(word)
        dic[word] = 1
for key in dic.keys():
    if len(key) == lenMax:
        print(key, dic[key])
