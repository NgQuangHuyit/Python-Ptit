while True:
    inp = input()
    if inp == '0':
        break
    K, s = inp.split()
    K = int(K)
    P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
    dic = {}
    for i in range(len(P)):
        dic[P[i]] = i
    res = ''
    for i in range(len(s)):
        res += P[(dic[s[i]] + K) % 28]
    res = list(res)
    res.reverse()
    print(''.join(res))