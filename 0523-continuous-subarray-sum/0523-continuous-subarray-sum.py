class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        # O(n)
        # O(n)
        n = len(nums)
        preSum = [0] * (n + 1)
        for i in range(n):
            preSum[i + 1] = preSum[i] + nums[i]
        
        val_to_index = {}
        for i in range(len(preSum)):
            val = preSum[i] % k
            if val not in val_to_index:
                val_to_index[val] = i
            
        for i in range(1, len(preSum)):
            need = preSum[i] % k
            if need in val_to_index:
                if i - val_to_index[need] >= 2:
                    return True
        
        return False