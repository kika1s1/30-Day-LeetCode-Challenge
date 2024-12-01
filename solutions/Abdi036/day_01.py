class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       hash_map = {}

       for i in range(len(nums)):
        hash_map[nums[i]] = i

       for i in range(len(nums)):
        num = target - nums[i]
        if(num in hash_map and hash_map[num] != i):
            return [i,hash_map[num]]
            
       return []
    


