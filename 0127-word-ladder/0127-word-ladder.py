class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # n: len(wordList)
        # l: len(beginWord)
        # O(nl^2)
        # O(nl)
        word_set = set(wordList)   # O(nl)
        if endWord not in word_set:
            return 0
        
        q = deque([(beginWord, 1)])
        visited = set([beginWord])    # O(l) -> hash
        while q:
            cur, steps = q.popleft()   # mostly O(n)
            if cur == endWord:         # O(l)
                return steps
            
            for i in range(len(cur)):     # -> O(l)
                for ch in "abcdefghijklmnopqrstuvwxyz":    # O(26)
                    new_word = cur[:i] + ch + cur[i + 1:]    # -> O(l)
                    if new_word not in word_set:
                        continue
                    if new_word in visited:
                        continue
                    
                    visited.add(new_word)
                    q.append((new_word, steps + 1))
        
        return 0