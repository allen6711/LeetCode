class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # O(nlogn)
        # O(1)
        # if not nums:
        #     return 0
        # nums.sort()
        # longest = 1
        # current = 1
        # n = len(nums)
        # for i in range(1, n):
        #     if nums[i] == nums[i - 1]:
        #         continue
        #     elif nums[i] == nums[i - 1] + 1:
        #         current += 1
        #     else:
        #         current = 1
        
        #     longest = max(longest, current)

        # return longest
        # O(n)
        # O(n)
        if not nums:
            return 0
        nums_set = set(nums)
        max_count = 0
        for num in nums_set:
            count = 1
            if num - 1 in nums_set:
                continue
            
            while num + 1 in nums_set:
                count += 1
                num += 1

            max_count = max(max_count, count)

        return max_count