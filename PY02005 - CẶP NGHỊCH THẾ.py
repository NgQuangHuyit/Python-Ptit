n = input()
nums = list(map(int, input().split()))
cnt = 0
for u in range(len(nums)-1):
    for v in range(u+1,len(nums)):
        if nums[u] > nums[v]:
            cnt += 1
print(cnt)
