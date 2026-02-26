class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # O(n^2)
        # O(1)
        # n = len(prices)
        # best = float('-inf')
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         diff = prices[j] - prices[i]
        #         best = max(best, diff)

        # return best if best > 0 else 0
        # O(n)
        # O(1)
        min_price = float('inf')
        best = 0
        for price in prices:
            min_price = min(min_price, price)
            best = max(best, price - min_price)
        
        return best
