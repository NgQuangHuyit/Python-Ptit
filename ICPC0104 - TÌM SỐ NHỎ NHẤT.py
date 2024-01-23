for t in range(int(input())):
    x = list(input())
    for i in range(len(x)):
        if x[i].isalpha():
            x[i] = ' '
    x = ''.join(x)
    res = min(map(int, x.split()))
    print(res)