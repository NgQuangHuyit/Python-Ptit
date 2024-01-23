for t in range(int(input())):
    N = map(int, list(input()))
    sum_of_digits = sum(N)
    if sum_of_digits % 3 == 0:
        print("YES")
    else:
        print("NO")
