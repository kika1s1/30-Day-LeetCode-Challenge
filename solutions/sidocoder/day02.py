class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        pointer1 = 0
        pointer2 = 1
        
        while pointer2 < len(nums):
            if nums[pointer1] == nums[pointer2]:
                return True
            pointer1 += 1
            pointer2 += 1
        
        return False
