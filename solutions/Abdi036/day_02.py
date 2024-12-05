class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}

        for i in range(len(nums)):
            if(nums[i] in hash_map):
                hash_map[nums[i]] += 1
            else:
                hash_map[nums[i]] = 1
        
        for key,value in hash_map.items():
            if(value >= 2):
                return True
        return False

