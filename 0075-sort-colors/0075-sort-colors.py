class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Counting Sort
        # O(n): O(n+n)
        # O(1)
        count = [0] * 3
        for num in nums:
            count[num] += 1
        
        index = 0
        for num in range(3):
            for _ in range(count[num]):
                nums[index] = num
                index += 1