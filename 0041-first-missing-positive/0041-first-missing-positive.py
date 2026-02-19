class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # O(n)
        # O(n)
        num_set = set(nums)
        x = 1
        while x in num_set:
            x += 1
        return x