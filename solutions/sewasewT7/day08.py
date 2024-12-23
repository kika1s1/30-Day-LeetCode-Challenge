class Solution(object):
    def minWindow(self, s, t):
        if not s or not t:
         return ""
    
        t_freq = Counter(t)
        window_freq = Counter()
        
        left = 0
        right = 0
        required_chars = len(t_freq)
        formed_chars = 0
        min_len = float('inf')
        min_window = ""
        
        while right < len(s):
            window_freq[s[right]] += 1
            
            if window_freq[s[right]] == t_freq[s[right]]:
                formed_chars += 1
            
            while left <= right and formed_chars == required_chars:
                window_len = right - left + 1
                if window_len < min_len:
                    min_len = window_len
                    min_window = s[left:right + 1]
                
                window_freq[s[left]] -= 1
                if window_freq[s[left]] < t_freq[s[left]]:
                    formed_chars -= 1
                left += 1
            
            right += 1
        
        return min_window