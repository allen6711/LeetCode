class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        # O(n)
        # O(n)
        n = len(heights)
        stack = []
        ans = 0

        for i in range(n + 1):
            h = heights[i] if i < n else 0
            while stack and heights[stack[-1]] >= h:
                height = heights[stack.pop()]  # previous

                left = stack[-1] if stack else -1
                width = i - left - 1

                ans = max(ans, height * width)
            
            if i < n:
                stack.append(i)
        
        return ans