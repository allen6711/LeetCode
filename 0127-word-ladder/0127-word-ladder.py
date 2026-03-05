class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
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
















        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        queue = deque([beginWord])
        distance = {beginWord: 1}

        while queue:
            word = queue.popleft()
            if word == endWord:
                return distance[word]
            
            for next_word in self.get_next_words(word):
                if next_word not in wordSet or next_word in distance:
                    continue
                queue.append(next_word)
                distance[next_word] = distance[word] + 1

        return 0

    def get_next_words(self, word: str):
        words = set()
        for i in range(len(word)):
            left, right = word[:i], word[i+1:]
            for char in 'abcdefghijklmnopqrstuvwxyz':
                if word[i] == char:
                    continue
                words.add(left + char + right)
    
        return words
