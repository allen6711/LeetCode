class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # O(n)
        # O(n)
        n = len(nums)
        preSum = [0] * (n + 1)
        preSum[0] = 0
        for i in range(n):
            preSum[i + 1] = preSum[i] + (-1 if nums[i] == 0 else 1)
        
        val_to_index = {}
        ans = 0

        for i in range(len(preSum)):
            if preSum[i] not in val_to_index:
                val_to_index[preSum[i]] = i
            else:
                ans = max(ans, i - val_to_index[preSum[i]])
        
        return ans