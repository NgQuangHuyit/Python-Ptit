dic = {'0': 1, '1': 1, '2':2, '3': 6, '4': 24, '5': 120, '6': 720, '7': 5040, '8': 40320, '9': 362880}
for t in range(int(input())):
    N = input()
    sumDigits = 0
    for digit in N:
        sumDigits += dic[digit]
    if sumDigits == int(N):
        print("Yes")
    else:
        print("No")
