class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, number in enumerate(nums):
            complement = target - number
            if complement in hashmap:
                return [hashmap[complement], index]
            hashmap[number] = index
        return []
