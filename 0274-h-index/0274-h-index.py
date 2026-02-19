class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        best = 0
        for i in range(1, n + 1):
            check = 0
            for num in citations:
                if num >= i:
                    check += 1
            
            if check >= i:
                best = max(best, i)
        
        return best