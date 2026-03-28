class Solution:
    def trap(self, height: List[int]) -> int:
        # O(n^2)
        # n = len(height)
        # ans = 0
        # for i in range(n):
        #     leftmax = 0
        #     rightmax = 0

        #     for l in range(i + 1):
        #         leftmax = max(leftmax, height[l])

        #     for r in range(i, n):
        #         rightmax = max(rightmax, height[r])

        #     ans += max(0, min(leftmax, rightmax) - height[i])
        
        # return ans

        # O(n)
        # O(1)
        n = len(height)
        leftmax = 0
        rightmax = 0
        left, right = 0, n - 1
        ans = 0
        while left < right:
            if height[left] <= height[right]:
                if height[left] > leftmax:
                    leftmax = height[left]
                else:
                    ans += leftmax - height[left]
                left += 1
            else:
                if height[right] > rightmax:
                    rightmax = height[right]
                else:
                    ans += rightmax - height[right]
                right -= 1
        return ans