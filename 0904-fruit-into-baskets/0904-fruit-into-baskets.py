class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # left = 0
        # best = float('-inf')
        # count = {}
        # left = 0
        # best_left = 0
        # for right, fruit in enumerate(fruits):
        #     count[fruit] += 1
















        # O(n)
        # O(k)
        left = 0
        count = {}
        best = 0
        for right, fruit in enumerate(fruits):
            if fruit in count:
                count[fruit] += 1
            else:
                count[fruit] = 1
            
            # Shrink window until it has at most 2 distinct fruit types
            while len(count) > 2:
                left_fruit = fruits[left]
                count[left_fruit] -= 1
                if count[left_fruit] == 0:
                    del count[left_fruit]
                left += 1
            best = max(best, right - left + 1)
        
        return best