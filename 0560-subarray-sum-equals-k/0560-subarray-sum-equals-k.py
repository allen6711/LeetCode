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
        count = defaultdict(int)
        count[0] = 1
        prefix = 0
        ans = 0
        for num in nums:
            prefix += num
            ans += count[prefix - k]
            count[prefix] += 1
        
        return ans

        # count = defaultdict(int)
        # count[0] = 1
        # prefix = 0
        # ans = 0

        # for num in nums:
        #     prefix += num
        #     ans += count[prefix - k]
        #     count[prefix] += 1

        # return ans

        # sum_dict = {0:1}
        # cumulative_sum = 0
        # count = 0

        # for num in nums:
        #     cumulative_sum += num
        #     count += sum_dict.get((cumulative_sum - k), 0)
        #     sum_dict[cumulative_sum] = 1 + sum_dict.get(cumulative_sum, 0)

        # return count