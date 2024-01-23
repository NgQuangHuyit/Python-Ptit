def check(num1, num2):
    if num1 == 1:
        print("YES")
        return
    while num1 != num2:
        if num1 > num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1
    if num1 == 1:
        print("YES")
    else:
        print("NO")

for t in range(int(input())):
    s1 = input()
    s2 = s1[::-1]
    check(int(s1), int(s2))
