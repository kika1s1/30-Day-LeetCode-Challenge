class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twosum = defaultdict(int)

        for i in range (len(nums)):
            com = target - nums[i]

            if com in twosum.keys() :
                return  [ twosum[com], i ]
            
            twosum[nums[i]] = i
