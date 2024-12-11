class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        check = len(s) == len(t) 
        anagram = False
        c = Counter(s)
        d = Counter(t) 
        if(check):    
            if(c == d):
                anagram = True
        return anagram