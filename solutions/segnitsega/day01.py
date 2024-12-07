class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            k = target - nums[i]
            nums[i] = ""
            if k in nums:
                j = nums.index(k)
                return [i, j]

        return []