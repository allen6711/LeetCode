class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        
        p_to_s = {}
        s_to_p = {}
        for ch, word in zip(pattern, words):
            if ch in p_to_s and p_to_s[ch] != word:
                return False
            if word in s_to_p and s_to_p[word] != ch:
                return False
            p_to_s[ch] = word
            s_to_p[word] = ch
        return True













        # O(n^2)
        # O(1)
        # words = s.split()
        # if len(pattern) != len(words):
        #     return False
        # n = len(pattern)
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if (pattern[i] == pattern[j] and words[i] != words[j]) or \
        #            (pattern[i] != pattern[j] and words[i] == words[j]):
        #            return False
        # return True
        # O(n)
        # O(n)
        words = s.split()
        if len(pattern) != len(words):
            return False
        p_to_s = {}
        s_to_p = {}
        for char, word in zip(pattern, words):
            if char in p_to_s and p_to_s[char] != word:
                return False
            if word in s_to_p and s_to_p[word] != char:
                return False
            p_to_s[char] = word
            s_to_p[word] = char

        return True