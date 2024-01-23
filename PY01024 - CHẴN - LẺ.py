for t in range(int(input())):
    N = list(map(int, list(input())))
    sum_of_digits = sum(N)
    ok = True
    if sum_of_digits % 10 == 0:
        for i in range(len(N)-1):
            if abs(N[i] - N[i+1]) != 2:
                ok = False
                break
    else:
        ok = False
    if ok :
        print("YES")
    else:
        print("NO")