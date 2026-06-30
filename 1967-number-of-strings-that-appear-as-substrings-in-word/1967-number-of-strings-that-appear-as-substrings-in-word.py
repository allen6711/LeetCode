class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        answer = 0
        for pattern in patterns:
            if pattern in word:
                answer += 1
        
        return answer
















        # n: number of patterns
        # m: length of word
        # k: average length of pattern
        # O(n*m*k)
        # O(1)
        answer = 0
        for pattern in patterns:
            if pattern in word:
                answer += 1
        
        return answer