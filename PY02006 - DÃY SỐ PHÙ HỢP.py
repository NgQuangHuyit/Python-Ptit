for t in range(int(input())):
    n = input()
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    ok = True
    for i in range(len(A)):
        if A[i] > B[i]:
            ok = False
            break
    if ok:
        print("YES")
    else:
        print("NO")
