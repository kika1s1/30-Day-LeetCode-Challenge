class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordSet = set(wordList)
        queue = deque([(beginWord, 1)])
        
        while queue:
            current_word, length = queue.popleft()
            
            if current_word == endWord:
                return length
            
            for i in range(len(current_word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = current_word[:i] + c + current_word[i+1:]
                    if next_word in wordSet:
                        queue.append((next_word, length + 1))
                        wordSet.remove(next_word)
        
        return 0
