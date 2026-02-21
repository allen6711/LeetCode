class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # O(n^2)
        # O(1)
        # left = 0
        # n = len(nums)
        # while left < n:
        #     if nums[left] == 0:
        #         nums.pop(left)
        #         nums.append(0)
        #         n -= 1
        #     else:
        #         left += 1
        # O(n)
        # O(1)
        # left = 0
        # n = len(nums)
        # for i in range(n):
        #     if nums[i] != 0:
        #         nums[left] = nums[i]
        #         left += 1
        
        # for i in range(left, n):
        #     nums[i] = 0
        
        # O(n)
        # O(1)
        left = 0
        n = len(nums)
        for i in range(n):
            if nums[i] != 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
