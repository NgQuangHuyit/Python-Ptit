for t in range(int(input())):
    l1, l2, l3 = map(int, input().split())
    set1 = [int(num) for num in input().split()]
    set2 = [int(num) for num in input().split()]
    set3 = [int(num) for num in input().split()]
    i1 = i2 = i3 = 0
    res = []
    while True:
        stop = False
        while set1[i1] < set2[i2]:
            i1 += 1
            if i1 == l1:
                stop = True
                break
        while set3[i3] < set2[i2]:
            i3 += 1
            if i3 == l3:
                stop = True
                break
        if stop:
            break
        if set1[i1] == set2[i2] and set2[i2] == set3[i3]:
            res.append(set1[i1])
            i2 += 1
            i1 += 1
            i3 += 1
        else:
            i2 += 1
        if i1 == l1 or i2 == l2 or i3 == l3:
            break
    if res:
        print(*res)
    else:
        print('NO')
