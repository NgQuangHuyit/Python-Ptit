for t in range(int(input())):
    p, q = sorted(input().split())
    nums = []
    while len(nums) < 2:
        nums.extend(input().split())
    X1 = nums[0]
    X2 = nums[1]
    print(int(X1.replace(q, p)) + int(X2.replace(q, p)), int(X1.replace(p, q)) + int(X2.replace(p, q)), sep=' ')
