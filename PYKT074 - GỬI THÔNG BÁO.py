for t in range(int(input())):
    noti = list(input())
    if len(noti) <= 100:
        print(''.join(noti))
    else:
        solved_noti = noti[:100]
        if noti[100] != ' ':
            while solved_noti[-1] != ' ':
                del solved_noti[-1]
        print(''.join(solved_noti))

