class Solution(object):
    def longestSubarray(self, nums):
        
        max_length = 0
        
        for i in range(len(nums)):
            temp = nums[:i] + nums[i+1:]
            current_len = 0
            longest = 0
            for num in temp:
                if num == 1:
                    current_len += 1
                    longest = max(longest, current_len)
                else:
                    current_len = 0
            
            # Update the maximum length
            max_length = max(max_length, longest)
        
        return max_length