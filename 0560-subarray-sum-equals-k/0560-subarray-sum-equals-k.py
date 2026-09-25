class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
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
        prefix_count = defaultdict(int)
        prefix_sum = 0
        prefix_count[prefix_sum] = 1
        ans = 0
        for num in nums:
            prefix_sum += num
            if prefix_sum - k in prefix_count:
                ans += prefix_count[prefix_sum - k]

            prefix_count[prefix_sum] += 1
        
        return ans