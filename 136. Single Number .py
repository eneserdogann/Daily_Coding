nums = nums = [4,1,2,1,2]

def singleNumber(nums):
    cple = 0
    for i in nums:
        cple ^= i

    return cple

print(singleNumber(nums))

