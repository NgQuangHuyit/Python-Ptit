def Try(n, k):
    if n == 1:
        return 1
    if k == (l[n] // 2 + 1):
        return n
    if k <= l[n-1]:
        return Try(n-1, k)
    else:
        return Try(n - 1, k - l[n - 1] - 1)


l = [0, 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575, 2097151, 4194303, 8388607, 16777215, 33554431]
dic ={}
for i in range(1, 26):
    dic[i] = chr(ord('A') + i - 1)
for t in range(int(input())):
    n, k = map(int, input().split())
    print(dic[Try(n, k)])


