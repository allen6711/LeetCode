class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        # first_cost = nums[0]
        # remaining_sorted = sorted(nums[1:])

        # return first_cost + remaining_sorted[0] + remaining_sorted[1]

        min1 = float('inf')
        min2 = float('inf')
        
        for x in nums[1:]:
            if x < min1:
                min2 = min1
                min1 = x
            elif x < min2:
                min2 = x
        
        return nums[0] + min1 + min2