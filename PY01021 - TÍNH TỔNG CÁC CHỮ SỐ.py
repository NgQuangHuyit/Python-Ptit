for t in range(int(input())):
    res = []
    sum_of_digits = 0
    for c in input():
        if c.isalpha():
            res.append(c)
        else:
            sum_of_digits += int(c)
    res.sort()
    res = ''.join(res)
    res += str(sum_of_digits)
    print(res)
