for t in range(int(input())):
    N = list(map(int, list(input())))
    sum_digits = 0
    product = 1
    zero = True
    for i in range(0, len(N), 2):
        sum_digits += N[i]
    for digit in range(1, len(N), 2):
        if N[digit] != 0:
            product *= N[digit]
            zero = False
    if zero:
        print(f"{sum_digits} 0")
    else:
        print(f"{sum_digits} {product}")
