class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        # n: number of patterns
        # m: length of m
        # k: average length of pattern
        # O(n*m*k)
        # O(1)
        answer = 0
        for pattern in patterns:
            if pattern in word:
                answer += 1
        
        return answer