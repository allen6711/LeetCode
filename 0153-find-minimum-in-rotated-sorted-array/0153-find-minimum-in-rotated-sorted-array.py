class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return -1
        
        start, end = 0, len(nums) - 1

        while start + 1 < end:
            mid = (start + end) // 2

            if nums[mid] < nums[-1]:
                end = mid
            
            elif nums[mid] > nums[-1]:
                start = mid
            
            else:
                end = mid

        return min(nums[start], nums[end])



























        # left, right = 0, len(nums) - 1
        # index = -1

        # while left <= right:
        #     mid = (left + right) // 2
        #     if nums[mid] <= nums[-1]:
        #         index = mid
        #         right = mid - 1
        #     else:
        #         left = mid + 1
        # return nums[index]