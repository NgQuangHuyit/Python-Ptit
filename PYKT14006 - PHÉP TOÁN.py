nm = []
while len(nm) < 2:
    nm += list(map(int, input().split()))
n, m = nm
arr = []
while len(arr) < n:
    arr += list(map(int, input().split()))
for i in range(len(arr)):
    if arr[i] < 0:
        tmp = "(" + str(arr[i]) + ")"
        arr[i] = tmp
    else:
        arr[i] = str(arr[i])
ok = False
o = [""] * (n-1)
operate = "+-*"
code = "{}".join(arr)


def Try(k):
    global o, ok
    for c in operate:
        o[k] = c
        if k == ((n-1) - 1):
            if eval(code.format(*o)) == m:
                ok = True
                print(code.format(*o) + f"={m}")
        else:
            Try(k + 1)


Try(0)
if not ok:
    print("IMPOSSIBLE")