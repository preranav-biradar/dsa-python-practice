def two_sum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[num] = i

print(two_sum([2, 7, 11, 15], 9)) 

#max_subarray.py
def max_subarray(nums):
    max_sum = current = nums[0]
    for num in nums[1:]:
        current = max(num, current + num)
        max_sum = max(max_sum, current)
    return max_sum

print(max_subarray([-2,1,-3,4,-1,2,1,-5,4])) 