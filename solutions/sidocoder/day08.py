from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        t_count = Counter(t)
        current_count = {}
        left = 0
        right = 0
        formed = 0
        required = len(t_count)
        min_length = float('inf')
        min_window = (0, 0)

        while right < len(s):
            char = s[right]
            current_count[char] = current_count.get(char, 0) + 1
            if char in t_count and current_count[char] == t_count[char]:
                formed += 1
            while left <= right and formed == required:
                char = s[left]
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    min_window = (left, right)
                current_count[char] -= 1
                if char in t_count and current_count[char] < t_count[char]:
                    formed -= 1

                left += 1
            right += 1

        left, right = min_window
        return s[left:right + 1] if min_length != float('inf') else ""
