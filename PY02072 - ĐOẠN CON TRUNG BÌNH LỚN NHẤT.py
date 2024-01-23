N = int(input()) + 1
arr = [int(x) for x in input().split()] + [-99]
max_avg_of_sub_arr = max(arr)
res = 0
tmp_res = 0
for i in range(len(arr)):
    if arr[i] == max_avg_of_sub_arr:
        tmp_res += 1
    else:
        res = max(tmp_res, res)
        tmp_res = 0
print(res)