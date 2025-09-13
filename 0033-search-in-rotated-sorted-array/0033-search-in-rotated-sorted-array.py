class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        start, end = 0, len(nums) - 1

        while start + 1 < end:
            mid = (start + end) // 2

            # we need two conditions to seperate the nums
            # [4, 5, 6, 7] and [0, 1, 2]
            # to control mid correctly
            if target <= nums[-1]:
                #[xxxxx012345]
                # 2 situations: nums[mid] in the first part or the second part
                # second part
                if target <= nums[mid] <= nums[-1]:
                    end = mid
                
                # nums[mid] < target or
                # nums[mid] > target and > nums[-1]
                # both should move start to mid
                else:
                    start = mid

            # target > nums[-1]
            else:
                if nums[-1] < nums[mid] <= target:
                    start = mid
                
                # target < nums[mid] or 
                # nums[mid] <= nums[-1]
                else:
                    end = mid
        
        if nums[start] == target:
            return start
        
        if nums[end] == target:
            return end

        return -1


























        # left, right = 0, len(nums) - 1
        # while left < right:
        #     mid = (left + right) // 2
        #     if nums[0] <= nums[mid]:
        #         if nums[0] <= target <= nums[mid]:
        #             right = mid
        #         else:
        #             left = mid + 1
        #     else:
        #         if nums[mid] < target <= nums[-1]:
        #             left = mid + 1
        #         else:
        #             right = mid
        
        # return left if nums[left] == target else -1
