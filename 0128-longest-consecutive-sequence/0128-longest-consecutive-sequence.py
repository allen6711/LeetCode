class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        current = 0
        longest = 0
        for num in num_set:
            if num - 1 not in num_set:
                current = num
                length = 1
                while current + 1 in num_set:
                    current += 1
                    length += 1
                longest = max(longest, length)
        
        return longest


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
        num_set = set(nums)
        longest = 0
        current = 0
        for num in num_set:
            if num - 1 not in num_set:  # find the sequence start
                current = num
                length = 1

                while current + 1 in num_set:
                    current += 1
                    length += 1
                
                longest = max(longest, length)
        return longest