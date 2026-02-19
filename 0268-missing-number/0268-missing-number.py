class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_set = set(nums)
        n = len(nums)
        for num in range(n + 1):
            if num not in num_set:
                return num
     