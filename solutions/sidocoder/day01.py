class Solution(object):
    def twoSum(self, nums, target):
        hash = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hash:
                return [hash[diff], i]
            hash[nums[i]] = i
        return 