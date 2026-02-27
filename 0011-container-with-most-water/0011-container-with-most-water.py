class Solution:
    def maxArea(self, height: List[int]) -> int:
        best = float('-inf')
        left, right = 0, len(height) - 1
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            best = max(best, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return best
















        # O(n^2)
        # O(1)
        # n = len(height)
        # best = float('-inf')
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         area = min(height[i], height[j]) * (j - i)
        #         best = max(best, area)
        
        # return best
        # O(n)
        # O(1)
        left, right = 0, len(height) - 1
        best = float('-inf')
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            best = max(best, area)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        
        return best
        # left, right = 0, len(height) - 1
        # best = float('-inf')
        # while left < right:
        #     area = min(height[left], height[right]) * (right - left)
        #     best = max(best, area)

        #     if height[left] > height[right]:
        #         right -= 1
        #     else:
        #         left += 1
        
        # return best

        # left, right = 0, len(height) - 1
        # max_area = 0
        # while left < right:
        #     area = min(height[left], height[right]) * (right - left)
        #     max_area = max(max_area, area)
        #     if height[left] <= height[right]:
        #         left += 1
        #     else:
        #         right -= 1
        
        # return max_area