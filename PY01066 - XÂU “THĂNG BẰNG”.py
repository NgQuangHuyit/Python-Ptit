for t in range(int(input())):
    s = input()
    rev = s[-1::-1]
    ok = True
    for i in range(len(s) - 1):
        if abs(ord(s[i]) - ord(s[i+1])) != abs(ord(rev[i]) - ord(rev[i+1])):
            ok = False
            break
    if ok:
        print('YES')
    else:
        print("NO")
