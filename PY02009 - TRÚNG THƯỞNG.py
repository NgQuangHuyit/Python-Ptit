for t in range(int(input())):
    dic = {}
    for i in range(int(input())):
        number = int(input())
        dic[number] = dic.setdefault(number, 0) + 1
    max_freq = max(dic.values())
    res = []
    keys = list(dic.keys())
    keys.sort()
    for key in keys:
        if dic[key] == max_freq:
            print(key)
            break
