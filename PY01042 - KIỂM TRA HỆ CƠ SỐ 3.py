for t in range(int(input())):
    N = list(input())
    ok = True
    for c in N:
        if c not in ['1', '2', '0']:
            ok = False
            break
    if ok:
        print("YES")
    else:
        print("NO")