def find_duplicate(nums):
    nums.sort()
    for index in range(1, len(nums)):
        if isinstance(nums[index], int) is False or nums[index] < 0:
            return False
        if nums[index] == nums[index - 1]:
            return nums[index]
    return False
