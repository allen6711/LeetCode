class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1

        left_max = 0
        right_max = 0

        water = 0

        while left < right:
            if height[left] < height[right]:
                left_max = max(left_max, height[left])
                water += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                water += right_max - height[right]
                right -= 1
        
        return water














        # O(n^2)
        # O(n)
        # n = len(height)
        # ans = 0

        # for i in range(n):
        #     leftmax = 0
        #     rightmax = 0

        #     for left in range(i + 1):
        #         leftmax = max(leftmax, height[left])
            
        #     for right in range(i, n):
        #         rightmax = max(rightmax, height[right])
            
        #     ans += min(leftmax, rightmax) - height[i]
        
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