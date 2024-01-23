for t in range(int(input())):
    N = input()
    ok = True
    if len(N) % 2 == 0:
        ok = False
    if ok:
        if N[0] == N[1]:
            ok = False
    if ok:
        last_digit = N[-1]
        for i in range(0, len(N), 2):
            if N[i] != last_digit:
                ok = False
                break
    if ok:
        print("YES")
    else:
        print("NO")
