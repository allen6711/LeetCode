class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        results = []
        nums.sort()

        for i in range(0, n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = n - 1

            while left < right:
                if nums[left] + nums[right] == -nums[i]:
                    results.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                        
                elif nums[left] + nums[right] < -nums[i]:
                    left += 1
                else:
                    right -= 1
        return results














        # n = len(nums)
        # results = []
        # nums.sort()

        # for i in range(0, n - 2):
        #     if i > 0 and nums[i] == nums[i - 1]:
        #         continue
            
        #     left = i + 1
        #     right = n - 1
        #     while left < right:
        #         target = -nums[i]
        #         if nums[left] + nums[right] == target:
        #             results.append([-target, nums[left], nums[right]])
        #             left += 1
        #             right -= 1
        #             while left < right and nums[left] == nums[left - 1]:
        #                 left += 1
        #             while left < right and nums[right] == nums[right + 1]:
        #                 right -= 1
        #         elif nums[left] + nums[right] > target:
        #             right -= 1
        #         else:
        #             left += 1
        
        # return results

    #     n = len(nums)
    #     results = []
    #     nums.sort()

    #     for i in range(0, n - 2):
    #         if i > 0 and nums[i] == nums[i - 1]:
    #             continue
    #         self.findTwoSum(nums, i + 1, n - 1, -nums[i], results)
        
    #     return results
    
    # def findTwoSum(self, nums, left, right, target, results):
    #     while left < right:
    #         if nums[left] + nums[right] == target:
    #             results.append((-target, nums[left], nums[right]))
    #             left += 1
    #             right -= 1
    #             while left < right and nums[left] == nums[left - 1]:
    #                 left += 1
    #             while left < right and nums[right] == nums[right + 1]:
    #                 right -= 1
            
    #         elif nums[left] + nums[right] < target:
    #             left += 1
            
    #         else:
    #             right -= 1
                
        # nums.sort()
        # n = len(nums)
        # triplets = []
        # for i in range(n - 2):
        #     # smallest > 0
        #     if nums[i] > 0:
        #         break
        #     # duplicate pass
        #     if i > 0 and nums[i] == nums[i - 1]:
        #         continue
        #     left, right = i + 1, n - 1
        #     while left < right:
        #         current_sum = nums[i] + nums[left] + nums[right]
        #         if current_sum < 0:
        #             left += 1
        #         elif current_sum > 0:
        #             right -= 1
        #         else:
        #             triplets.append([nums[i], nums[left], nums[right]])
        #             left, right = left + 1, right - 1
        #             while left < right and nums[left] == nums[left - 1]:
        #                 left += 1
        #             while left < right and nums[right] == nums[right + 1]:
        #                 right -= 1
        
        # return triplets