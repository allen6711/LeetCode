class Solution:
    def trap(self, height: List[int]) -> int:
        # O(n^2)
        # n = len(height)
        # ans = 0
        # for i in range(n):
        #     leftmax = float('-inf')
        #     for l in range(i, -1, - 1):
        #         leftmax = max(leftmax, height[l])
        #     rightmax = float('-inf')
        #     for r in range(i, n):
        #         rightmax = max(rightmax, height[r])

        #     ans += max(0, min(leftmax, rightmax) - height[i])
        
        # return ans

        # O(n)
        water = 0
        leftmax = float('-inf')
        rightmax = float('-inf')
        left, right = 0, len(height) - 1
        while left < right:
            if height[left] <= height[right]:
                if height[left] > leftmax:
                    leftmax = height[left]
                else:
                    water += leftmax - height[left]
                left += 1
            else:
                if height[right] > rightmax:
                    rightmax = height[right]
                else:
                    water += rightmax - height[right]
                right -= 1
        
        return water


        # max_left = 0
        # max_right = 0
        # left, right = 0, len(height) - 1
        # water = 0
        # while left < right:
        #     if height[left] <= height[right]:
        #         if height[left] > max_left:
        #             max_left = height[left]
        #         else:
        #             water += max_left - height[left]
        #         left += 1
        #     else:
        #         if height[right] > max_right:
        #             max_right = height[right]
        #         else:
        #             water += max_right - height[right]
        #         right -= 1
        
        # return water
        
        # left, right = 0, len(height) - 1
        # leftMax, rightMax = 0, 0
        # water = 0

        # while left < right:
        #     if height[left] <= height[right]:
        #         if height[left] >= leftMax:
        #             leftMax = height[left]
        #         else:
        #             water += leftMax - height[left]
        #         left += 1
        #     else:
        #         if height[right] >= rightMax:
        #             rightMax = height[right]
        #         else:
        #             water += rightMax - height[right]
        #         right -= 1
        
        # return water
            