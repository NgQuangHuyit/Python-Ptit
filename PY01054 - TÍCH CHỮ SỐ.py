for t in range(int(input())):
    N = map(int, list(input()))
    product_of_digits = 1
    for i in N:
        if i != 0:
            product_of_digits *= i
    print(product_of_digits)
