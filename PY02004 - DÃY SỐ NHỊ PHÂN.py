N = input()
nums = input().split()
cnt = 0
for i in range(len(nums)-1):
    if nums[i] != nums[i+1]:
        cnt += 1
print(cnt)
