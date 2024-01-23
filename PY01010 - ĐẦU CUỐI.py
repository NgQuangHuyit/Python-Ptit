for i in range(int(input())):
    n = input()
    if n[:2] == n[len(n)-2:]:
        print("YES")
    else:
        print("NO")