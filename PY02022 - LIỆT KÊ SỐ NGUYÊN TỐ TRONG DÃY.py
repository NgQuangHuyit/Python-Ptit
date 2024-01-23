N = int(input())
nums = list(map(int, input().split()))
max_num = max(nums)
# Sang nguyen to
is_prime = [True] * (max_num + 1)
is_prime[1] = False
is_prime[0] = False
for i in range(2, max_num + 1):
    if is_prime[i]:
        for j in range(i * i, max_num +1, i):
            is_prime[j] = False
dic = {}
for i in range(len(nums)):
    if is_prime[nums[i]]:
        dic[nums[i]] = dic.setdefault(nums[i], 0) + 1
for key in dic:
    print(f"{key} {dic[key]}")
