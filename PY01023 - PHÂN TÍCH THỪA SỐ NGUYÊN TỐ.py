def phantich(number):
    if number == 1:
        print(1)
        return
    dic = {}
    while number % 2 == 0:
        number /= 2
        dic[2] = dic.setdefault(2, 0) + 1
    factor = 3
    while number != 1:
        while number % factor == 0:
            number /= factor
            dic[factor] = dic.setdefault(factor, 0) + 1
        factor += 2
    res = list(dic.items())
    if len(res) != 0:
        print("1 * ", end='')
    else:
        print("1")
    for i in range(len(res)):
        if i != len(res) - 1:
            print("{}^{} * ".format(res[i][0], res[i][1]), end='')
        else:
            print("{}^{}".format(res[i][0], res[i][1]))


for t in range(int(input())):
    N = int(input())
    phantich(N)
