class Solution:
    def canSeePersonsCount(self, heights: list[int]) -> list[int]:
        # O(n)
        # O(n)
        n = len(heights)
        ans = [0] * n
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and heights[i] > stack[-1]:
                stack.pop()
                ans[i] += 1
            
            if stack:    # 右邊那個比他高的人
                ans[i] += 1

            stack.append(heights[i])
        
        return ans