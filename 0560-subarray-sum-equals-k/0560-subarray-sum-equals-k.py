class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # n = len(nums)
        # preSum = [0] * (n + 1)
        # count = {0: 1}
        # ans = 0

        # for i in range(n):
        #     preSum[i + 1] = preSum[i] + nums[i]

        #     if preSum[i + 1] - k in count:
        #         ans += count[preSum[i + 1] - k]
            
        #     if preSum[i + 1] not in count:
        #         count[preSum[i + 1]] = 1
        #     else:
        #         count[preSum[i + 1]] += 1
        
        # return ans
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