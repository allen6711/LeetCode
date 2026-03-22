class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest = 0
        current_end = 0
        jumps = 0
        n = len(nums)
        for i in range(n - 1):
            if i > farthest:
                return -1
            farthest = max(farthest, i + nums[i])

            if i == current_end:
                jumps += 1
                current_end = farthest
        
        return jumps
            














        # O(n)
        # O(1)
        jumps = 0
        farthest = 0
        current_end = 0
        n = len(nums)
        for i in range(n - 1):
            if i > farthest:
                return -1
            farthest = max(farthest, i + nums[i])   

            if i == current_end:
                jumps += 1
                current_end = farthest

        return jumps 