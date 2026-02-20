class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # O(n^2)
        # O(1)
        # n = len(citations)
        # best = 0
        # for i in range(1, n + 1):
        #     check = 0
        #     for num in citations:
        #         if num >= i:
        #             check += 1
            
        #     if check >= i:
        #         best = max(best, i)
        
        # return best
        # O(nlogn)
        # O()
        citations.sort(reverse = True)
        h = 0
        for i, num in enumerate(citations):
            if num >= i + 1:
                h = i + 1
            else:
                break
        
        return h