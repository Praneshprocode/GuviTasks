
nums = [10, 20, 30, 9]
target = 59
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        for k in range(j + 1, len(nums)):
            if nums[i] + nums[j] + nums[k] == target:
                print(nums[i], nums[j], nums[k])