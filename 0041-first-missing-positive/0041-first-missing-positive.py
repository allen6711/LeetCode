class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # O(n)
        # O(n)
        # num_set = set(nums)
        # x = 1
        # while x in num_set:
        #     x += 1
        # return x
        # O(n)
        # O(1)
        n = len(nums)
        for i in range(n):
            if nums[i] > n or nums[i] < 1:
                nums[i] = n + 1
        
        for i in range(n):
            x = abs(nums[i])
            if x <= n:
                nums[x - 1] = -abs(nums[x - 1])

        for i in range(n):
            if nums[i] > 0:
                return i + 1
        
        return n + 1