nums = [1,3,5,6]
target = 5

def searchInsert(nums, target):
    if target <= nums[0]:
        return 0

    for i in nums[::-1]:
        if i == target:
            index = nums.index(i)
            return index
        elif i <= target:
            index = nums.index(i)
            return index + 1

print(searchInsert(nums, target))