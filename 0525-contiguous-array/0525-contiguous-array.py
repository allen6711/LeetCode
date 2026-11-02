class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
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















        # O(n)
        # O(n)
        first_seen = {0: -1}
        prefix_sum = 0
        max_length = 0

        for i, num in enumerate(nums):
            if num == 0:
                prefix_sum -= 1
            else:
                prefix_sum += 1
            
            if prefix_sum in first_seen:
                max_length = max(max_length, i - first_seen[prefix_sum])
            else:
                first_seen[prefix_sum] = i
        
        return max_length