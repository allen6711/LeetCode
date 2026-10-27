class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # O(logn)
        # O(1)
        n = len(nums)
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        
        if nums[left] == target:
            return left
        
        return -1