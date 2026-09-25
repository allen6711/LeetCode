class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_count = defaultdict(int)
        prefix_count[0] = 1
        prefix_sum = 0
        ans = 0
        for num in nums:
            prefix_sum += num
            if prefix_sum - k in prefix_count:
                ans += prefix_count[prefix_sum - k]
            
            prefix_count[prefix_sum] += 1
        
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
        count = defaultdict(int)
        count[0] = 1
        prefix = 0
        ans = 0
        for num in nums:
            prefix += num
            ans += count[prefix - k]
            count[prefix] += 1
        
        return ans