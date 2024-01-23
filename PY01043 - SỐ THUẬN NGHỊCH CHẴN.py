def list_palindromic_bf_nums(limit:int) -> list:
    res = []
    for i in range(22, limit, 2):
        str_num = str(i)
        if len(str_num) % 2 == 1:
            continue
        if all(int(digit) % 2 == 0 for digit in str_num):
            if str_num == str_num[-1::-1]:
                res.append(i)
        else:
            continue
    return res


for i in range(int(input())):
    N = int(input())
    nums = list_palindromic_bf_nums(limit=N)
    print(*nums)