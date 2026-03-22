class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        n = len(nums)
        for i in range(n):
            if i > farthest:
                return False
            farthest = max(farthest, nums[i] + i)
            if farthest >= n - 1:
                return True
        














        # O(n)
        # O(1)
        farthest = 0
        n = len(nums)

        for i in range(n):
            # current i compares with previous farthest
            if i > farthest:
                return False
            farthest = max(farthest, i + nums[i])
        
            if farthest >= n - 1:
                return True
