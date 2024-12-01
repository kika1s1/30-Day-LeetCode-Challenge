class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        l = 0
        r = n - 1
        while l < r:
            summ = nums[l] + nums[r]
            if summ == target:
                return[l,r]
            elif summ < target:
                l += 1
            else:
                r -= 1
               