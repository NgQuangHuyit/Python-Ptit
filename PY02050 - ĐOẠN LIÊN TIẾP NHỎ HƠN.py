for t in range(int(input())):
    N = int(input())
    nums = list(map(int, input().split()))
    res = [1] * len(nums)
    for i in range(1, len(nums)):
        j = i - 1
        while j >= 0 and nums[i] >= nums[j]:
            res[i] += res[j]
            j -= res[j]
    print(*res)
