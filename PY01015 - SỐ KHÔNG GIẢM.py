for i in range(int(input())):
    digits = list(input())
    if digits == sorted(digits):
        print("YES")
    else:
        print("NO")
