for t in range(int(input())):
    inp = input()
    s1 = list(inp)
    s2 = list(inp)
    s2.reverse()
    ok = True
    for i in range(1, len(s1)):
        if abs(ord(s1[i]) - ord(s1[i-1])) != abs(ord(s2[i]) - ord(s2[i-1])):
            ok = False
            break
    if not ok:
        print("NO")
    else:
        print("YES")
