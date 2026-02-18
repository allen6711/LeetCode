class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # O(n)
        # O(n)
        s = set(nums)
        best = 0
        for num in s:
            if num - 1 in s:
                continue    # not a sequence start
            num2 = num
            while num2 in s:
                num2 += 1
            
            best = max(best, num2 - num)  # length
            
        return best



















        if not nums:
            return 0

        num_set = set(nums)
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

        # if not nums:
        #     return 0

        # num_set = set(nums)
        # longest = 0

        # for num in num_set:
        #     if num - 1 not in num_set:
        #         current = num
        #         length = 1

        #         while current + 1 in num_set:
        #             current += 1
        #             length += 1

        #         longest = max(longest, length)
        
        # return longest

        # if not nums:
        #     return 0

        # num_set = set(nums)
        # longest = 0

        # for num in num_set:
        #     if num - 1 not in num_set:
        #         current = num
        #         length = 1

        #         while current + 1 in num_set:
        #             current += 1
        #             length += 1
                
        #         longest = max(longest, length)
        
        # return longest

        # num_set = set(nums)
        # longest_streak = 0

        # for num in num_set:
        #     if num - 1 not in num_set:
        #         current_num = num
        #         current_streak = 1
        #         while current_num + 1 in num_set:
        #             current_num += 1
        #             current_streak += 1
                
        #         longest_streak = max(longest_streak, current_streak)
        
        # return longest_streak