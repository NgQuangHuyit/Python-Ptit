for t in range(int(input())):
    N = list(map(int, list(input())))
    sum_digits = 0
    product = 1
    for i in range(1, len(N), 2):
        sum_digits += N[i]
    for i in range(0, len(N), 2):
        if N[i] != 0:
            product *= N[i]
    print(f"{product} {sum_digits}")
