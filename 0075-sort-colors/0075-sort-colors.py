class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Counting Sort
        # O(n): O(n+n)
        # O(1)
        # count = [0] * 3
        # for num in nums:
        #     count[num] += 1
        
        # index = 0
        # for num in range(3):
        #     for _ in range(count[num]):
        #         nums[index] = num
        #         index += 1
        # Dutch National Flag (Three Pointers)
        # 
        left = 0
        mid = 0
        right = len(nums) - 1
        while mid <= right:
            if nums[mid] == 0:
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[right] = nums[right], nums[mid]
                right -= 1