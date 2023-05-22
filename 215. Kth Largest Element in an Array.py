nums = [3,2,1,5,6,4]
k = 2


def findKthLargest(nums, k):
    nums.sort()
    nums = nums[::-1]

    return nums[k - 1]

print(findKthLargest(nums, k))