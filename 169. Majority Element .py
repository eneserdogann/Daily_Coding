nums = [2,2,1,1,1,2,2,3,3,3,3,3]

def majorityElement(nums):
    return max(set(nums), key=nums.count)

print(majorityElement(nums))

