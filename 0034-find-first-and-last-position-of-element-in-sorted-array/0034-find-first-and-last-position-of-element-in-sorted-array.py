class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        # O(logn)
        # O(1)
        n = len(nums)

        def find_left(nums: list[int], target: int) -> int:
            left = 0
            right = n - 1
            ans = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
                
                if nums[mid] == target:
                    ans = mid
            
            return ans
        
        def find_right(nums: list[int], target: int) -> int:
            left = 0
            right = n - 1
            ans = -1
            while left <= right:
                mid = (left + right + 1) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1

                if nums[mid] == target:
                    ans = mid
            
            return ans

        return [find_left(nums, target), find_right(nums, target)]
