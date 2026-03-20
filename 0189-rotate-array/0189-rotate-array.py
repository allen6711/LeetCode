class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        n = len(nums)
        k %= n
        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)
    
    def reverse(self, nums: list(int), left: int, right: int) -> None:
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        # O(n)
        # O(n)
        # n = len(nums)
        # k %= n
        # res = [0] * n

        # for i in range(n):
        #     # move k step to right
        #     res[(i + k) % n] = nums[i]
        
        # for i in range(n):
        #     nums[i] = res[i]
        
        # O(n)
        # O(1)
    #     if not nums:
    #         return
    #     n = len(nums)
    #     k %= n
    #     self.reverse(0, n - 1, nums)
    #     self.reverse(0, k - 1, nums)
    #     self.reverse(k, n - 1, nums)

    # def reverse(self, left: int, right: int, nums: list[int]) -> None:
    #     while left < right:
    #         nums[left], nums[right] = nums[right], nums[left]
    #         left += 1
    #         right -= 1
        

         