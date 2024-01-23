diem = [0.0, 0.0, 0.0, 2.5, 2.5, 3.0, 3.0, 3.5, 3.5, 3.5, 4.0, 4.0, 4.0, 4.5, 4.5, 4.5, 5.0, 5.0, 5.0, 5.0, 5.5, 5.5, 5.5, 6.0, 6.0, 6.0, 6.0, 6.5, 6.5, 6.5, 7.0, 7.0, 7.0, 7.5, 7.5, 8.0, 8.0, 8.5, 8.5, 9.0, 9.0]
for t in range(int(input())):
    reading, listening, speaking, writing = input().split()
    total = diem[int(reading)] + diem[int(listening)] + float(speaking) + float(writing)
    total /= 4
    d1 = int(total)
    d2 = total - float(d1)
    if d2 >= 0.75:
        d1 += 1
        d2 = 0
    elif d2 >= 0.25:
        d2 = 0.5
    else:
        d2 = 0
    final = d1 + d2
    print(f"{final:.1f}")

