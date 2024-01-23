for i in range(int(input())):
    N = input()
    if len(N) == 1:
        print(N)
        continue
    rounding_threshold = int(N[0] + '4' * (len(N) - 2) + '5')
    if int(N) < rounding_threshold:
        res = int(N[0]) * 10 ** (len(N) - 1)
        print(res)
    else:
        res = (int(N[0]) + 1) * 10 ** (len(N) - 1)
        print(res)
