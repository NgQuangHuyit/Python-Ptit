for t in range(int(input())):
    s = input()
    cnt = 1
    for i in range(len(s)):
        if i <= (len(s) -2):
            if s[i] != s[i + 1]:
                print(str(cnt) + s[i], end='')
                cnt = 1
            else:
                cnt += 1
        else:
            print(str(cnt) + s[i], end='')
    print()
