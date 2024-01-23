for t in range(int(input())):
    N = list(input())
    if len(set(N)) > 2:
        print("NO")
        continue
    ok = True
    for i in range(len(N)-1):
        if N[i] == N[i+1]:
            ok = False
            break
    if ok:
        print("YES")
    else:
        print("NO")
