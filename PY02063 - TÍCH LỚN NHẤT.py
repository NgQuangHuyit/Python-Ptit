n = int(input())
a = sorted([int(x) for x in input().split()])
print(max(a[0] * a[1], a[-1] * a[-2], a[0] * a[1] * a[-1], a[-1] * a[-2] * a[-3]))
'''
case:
+ + + => 3 so duong lon nhat
+ + - => + + => 2 so duong lon nhat
+ - - => 2 so am nho nhat va so duong lon nhat
- - - => - - => 2 so am nho nhat
'''