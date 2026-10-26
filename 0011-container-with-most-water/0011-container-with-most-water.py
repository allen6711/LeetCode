class Solution:
    def maxArea(self, height: List[int]) -> int:
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
        n = len(height)
        left = 0
        right = n - 1
        area = 0
        while left < right:
            width = right - left
            area = max(area, width * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return area