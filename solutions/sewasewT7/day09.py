class Solution(object):
    def numberOfSubarrays(self, nums, k):
        prefix_count = {0: 1}
        count = 0
        odd_count = 0

        for num in nums:
            if num % 2 != 0:
                odd_count += 1
            
            if odd_count - k in prefix_count:
                count += prefix_count[odd_count - k]
            
            prefix_count[odd_count] = prefix_count.get(odd_count, 0) + 1

        return count
