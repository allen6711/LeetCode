class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        
        q = deque([(beginWord, 1)])
        visited = set([beginWord])
        while q:
            word, steps = q.popleft()
            if word == endWord:
                return steps
            word_char = list(word)
            for i in range(len(word_char)):
                original_char = word_char[i]
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    if ch == word_char[i]:
                        continue
                    word_char[i] = ch
                    candidate = "".join(word_char)
                    if candidate in word_set and candidate not in visited:
                        visited.add(candidate)
                        q.append((candidate, steps + 1))

                    word_char[i] = original_char

        return 0

        # O(nl)
        # O(n)
        word_set = set(wordList)

        # If endWord is not in the dictionary, no valid transformation exists
        if endWord not in word_set:
            return 0

        q = deque([(beginWord, 1)])
        visited = set([beginWord])

        while q:
            word, steps = q.popleft()
            if word == endWord:
                return steps

            # Convert to list once for easier character replacement
            word_chars = list(word)
            for i in range(len(word_chars)):
                original_char = word_chars[i]

                # Try replacing word[i] with 'a' to 'z'
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    if ch == original_char:
                        continue
                    
                    word_chars[i] = ch
                    candidate = "".join(word_chars)

                    if candidate in word_set and candidate not in visited:
                        visited.add(candidate)
                        q.append((candidate, steps + 1))
                
                # Restore original character before moving to next index
                word_chars[i] = original_char

        return 0