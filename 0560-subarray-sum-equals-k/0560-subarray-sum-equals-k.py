class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        preSum = [0] * (n + 1)
        for i in range(n):
            preSum[i + 1] = preSum[i] + nums[i]
        
        preSum_count = {0: 1}
        ans = 0
        for i in range(1, len(preSum)):
            if preSum[i] - k in preSum_count:
                ans += preSum_count[preSum[i] - k]
            if preSum[i] not in preSum_count:
                preSum_count[preSum[i]] = 1
            else:
                preSum_count[preSum[i]] += 1
        
        return ans
        # O(n^2)
        # O(1)
        # n = len(nums)
        # count = 0
        # for i in range(n):
        #     total = 0
        #     for j in range(i, n):
        #         total += nums[j]
        #         if total == k:
        #             count += 1
        # return count
        # O(n)
        # O(n)
        prefix_sum = 0
        prefix_count = {0: 1}
        count = 0
        
        for num in nums:
            prefix_sum += num
            if prefix_sum - k in prefix_count:
                count += prefix_count[prefix_sum - k]

            prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1
        
        return count