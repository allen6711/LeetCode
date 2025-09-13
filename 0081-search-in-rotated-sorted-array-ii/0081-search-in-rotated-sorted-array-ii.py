class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False

        start, end = 0, len(nums) - 1

        while start + 1 < end:
            mid = (start + end) // 2

            if target < nums[end]:
                if nums[mid] <= target:
                    start = mid
                
                elif target < nums[mid] < nums[end]:
                    end = mid
                
                # nums[mid] == nums[end] or
                # target not in nums
                else:
                    end -= 1
            
            elif nums[end] < target:
                if target <= nums[mid]:
                    end = mid

                elif nums[end] < nums[mid] < target:
                    start = mid
                
                # nums[mid] == nums[end] or 
                # target not in nums
                else:
                    end -= 1
            
            # nums[end] == target
            else:
                return True
        
        if nums[start] == target:
            return True

        if nums[end] == target:
            return True

        return False
            




        # if not nums:
        #     return False

        # start, end = 0, len(nums) - 1

        # while start + 1 < end:
        #     mid = (start + end) // 2

        #     if target < nums[end]:
        #         if nums[mid] <= target:
        #             start = mid
                
        #         elif target < nums[mid] < nums[end]:
        #             end = mid
                
        #         # nums[mid] == nums[end] or 
        #         # target not in the nums
        #         else:
        #             end -= 1
            
        #     elif nums[end] < target:
        #         if target <= nums[mid]:
        #             end = mid
                
        #         elif nums[end] < nums[mid] < target:
        #             start = mid
                
        #         # nums[mid] == nums[end] or
        #         # target not in the nums
        #         else:
        #             end -= 1
            
        #     # target == nums[end]
        #     else:
        #         return True
        
        # if nums[start] == target:
        #     return True

        # if nums[end] == target:
        #     return True
        
        # return False



        