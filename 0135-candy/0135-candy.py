class Solution:
    def candy(self, ratings: List[int]) -> int:
        # O(n^2)
        # O(n)
        # n = len(ratings)
        # candies = [1] * n
        
        # changed = True
        # while changed:
        #     changed = False
        #     for i in range(n):
        #         if i > 0 and ratings[i] > ratings[i - 1] and candies[i] <= candies[i - 1]:
        #             candies[i] = candies[i - 1] + 1
        #             changed = True
        #         if i < n - 1 and ratings[i] > ratings[i + 1] and candies[i] <= candies[i + 1]:
        #             candies[i] = candies[i + 1] + 1
        #             changed = True
        # return sum(candies)
        # O(n)
        # O(n)
        n = len(ratings)
        candies = [1] * n
        # Left to right: satisfy left neighbor rule
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        
        # Right to left: satisfy right neighbor rule
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        
        return sum(candies)
        
        