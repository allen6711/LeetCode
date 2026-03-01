class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
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















        window = Counter()
        left = 0
        best_left = 0
        best_len = float('-inf')
        basket = []
        for right, num in enumerate(fruits):
            window[num] += 1
            if len(window) == 2:
                window_len = right - left + 1
                if window_len > best_len:
                    best_len = window_len
                    best_left = left
                    basket = fruits[best_left:best_left + window_len]
                
            
            while len(window) > 2:
                window[num] -= 1
                left += 1
                break
        
        return 0 if best_len == float('-inf') else len(basket)