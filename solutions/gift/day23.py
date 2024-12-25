class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_map = {}

        for word in strs:
            # Create a hashmap key based on character counts
            key = tuple(sorted(word))
            if key not in anagrams_map:
                anagrams_map[key] = []
            anagrams_map[key].append(word)
        
        return list(anagrams_map.values())
