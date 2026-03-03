class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        left = 0
        best = float('-inf')
        count = {}
        for right in range(n):
            if fruits[right] in count:
                count[fruits[right]] += 1
            else:
                count[fruits[right]] = 1
            while len(count) > 2:
                left_num = fruits[left]
                count[left_num] -= 1
                if count[left_num] == 0:
                    del count[left_num]
                left += 1
            best = max(best, right - left + 1)
        
        return best
        # O(n^2)
        # O(k)
        # n = len(fruits)
        # best = float('-inf')
        # for i in range(n):
        #     count = {}
        #     for j in range(i, n):
        #         if fruits[j] in count:
        #             count[fruits[j]] += 1
        #         else:
        #             count[fruits[j]] = 1
                
        #         if len(count) > 2:
        #             break
        #         best = max(best, j - i + 1)
        # return best
        # O(n)
        # O(k)
        left = 0
        count = {}
        best = float('-inf')
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