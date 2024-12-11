class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                substring = s[i:j]
                if len(substring) == len(set(substring)):
                    max_length = max(max_length, len(substring))
        
        return max_length