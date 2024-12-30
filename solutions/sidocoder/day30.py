from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)
        pattern_map = defaultdict(list)
        word_length = len(beginWord)
        
        for word in wordList:
            for i in range(word_length):
                pattern = word[:i] + "*" + word[i+1:]
                pattern_map[pattern].append(word)
        
        queue = deque([(beginWord, 1)])
        visited = set()
        visited.add(beginWord)
        
        while queue:
            current_word, length = queue.popleft()
            
            for i in range(word_length):
                pattern = current_word[:i] + "*" + current_word[i+1:]
                
                for neighbor in pattern_map[pattern]:
                    if neighbor == endWord:
                        return length + 1
                    
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, length + 1))
                
                pattern_map[pattern] = []
        
        return 0
