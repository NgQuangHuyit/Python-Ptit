def check(a, b):
    while b:
        a, b = b, a % b
    if a == 1:
        return True
    else:
        return False


L, R = map(int, input().split())
for a in range(L, R-1):
    for b in range(a + 1, R):
        for c in range(b+1, R+1):
            if check(a,b) and check(a,c) and check(b,c):
                print(f"({a}, {b}, {c})")
