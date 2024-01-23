for t in range(int(input())):
    number = input()
    N = input()
    start_point = 0
    cnt = 0
    while number.find(N, start_point) != -1 and start_point < len(number):
        cnt += 1
        start_point = number.find(N, start_point) + len(N)
    print(cnt)
