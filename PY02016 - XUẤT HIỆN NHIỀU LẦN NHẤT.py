for t in range(int(input())):
    N = int(input())
    nums = list(map(int, input().split()))
    dic = {}
    for num in nums:
        dic[num] = dic.setdefault(num, 0) + 1
    keys = list(dic.keys())
    keys.sort()
    ok = False
    for key in keys:
        if dic[key] > N/2:
            print(key)
            ok = True
            break
    if not ok:
        print('NO')
