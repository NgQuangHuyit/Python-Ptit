for t in range(int(input())):
    N = map(int, list(input()))
    sum_of_digits = sum(N)
    if str(sum_of_digits) == str(sum_of_digits)[::-1] and sum_of_digits >= 10:
        print("YES")
    else:
        print("NO")
