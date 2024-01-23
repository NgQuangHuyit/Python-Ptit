s = input()
freq = {}
for i in range(0, len(s), 2):
    if i == len(s) - 1:
        break
    num = s[i] + s[i+1]
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
for key in freq:
    print(f"{key} {freq[key]}")
