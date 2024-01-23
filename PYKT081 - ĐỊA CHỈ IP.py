for t in range(int(input())):
    try:
        ip = [int(i) for i in input().split(sep='.')]
        ok = True
        if len(ip) != 4:
            ok = False
        if ok:
            for num in ip:
                if num < 0 or num > 255:
                    ok = False
                    break
        if ok:
            print('YES')
        else:
            print('NO')

    except:
        print('NO')
