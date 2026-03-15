class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # O(n)
        # O(n)
        n = len(nums)
        k %= n
        res = [0] * n

        for i in range(n):
            res[(i + k) % n] = nums[i]
        
        for i in range(n):
            nums[i] = res[i]

         