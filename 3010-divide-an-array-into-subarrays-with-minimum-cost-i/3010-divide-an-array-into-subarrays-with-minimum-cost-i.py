class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        first_cost = nums[0]
        remaining_sorted = sorted(nums[1:])

        return first_cost + remaining_sorted[0] + remaining_sorted[1]