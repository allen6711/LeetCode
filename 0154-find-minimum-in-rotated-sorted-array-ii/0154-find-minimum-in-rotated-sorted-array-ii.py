class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return -1
        
        start, end = 0, len(nums) - 1

        while start + 1 < end:
            mid = (start + end) // 2

            if nums[mid] < nums[end]:
                end = mid
            
            elif nums[end] < nums[mid]:
                start = mid
            
            else:
                end -= 1
        
        # start might be less than end
        return min(nums[start], nums[end])



























        # if not nums:
        #     return -1
        
        # start, end = 0, len(nums) - 1

        # while start + 1 < end:
        #     mid = (start + end) // 2

        #     # [2, 2, 2, 0, 1, 2]
        #     # [3, 3, 1, 3]
        #     if nums[mid] < nums[end]:
        #         end = mid
            
        #     elif nums[mid] > nums[end]:
        #         start = mid
            
        #     else:
        #         end -= 1
            
        # return min(nums[start], nums[end])



        # if not nums:
        #     return -1
        
        # start, end = 0, len(nums) - 1

        # while start + 1 < end:
        #     mid = (start + end) // 2

        #     # since the nums[-1] might be same as other element, we should dynamic update
        #     if nums[mid] < nums[end]:
        #         end = mid
            
        #     elif nums[mid] > nums[end]:
        #         start = mid
            
        #     else:    # nums[mid] == nums[-1], we are not sure the position
        #         end -= 1
            
        # return min(nums[start], nums[end])
                
        # brute-force
        # min = float('inf')

        # for num in nums:
        #     if num < min:
        #         min = num
        
        # return min